# Compress all python files in a directory and its subdirectories into a single JSON file
# Scan for certain txt files and store them as system prompts

import os
import json
import ast

def read_system_prompts(directory_path):
    """
    Walk through a directory and subdirectories to find all .txt files
    containing system prompts and return their contents.
    
    :param directory_path: Path to the directory to search for text files.
    :return: List of dictionaries containing prompt metadata and content.
    """
    prompts = []
    
    for root, dirs, files in os.walk(directory_path):
        for file_name in files:
            if file_name.endswith(".txt") and ("prompt" in file_name or "fact" in file_name or "hint" in file_name):
                file_path = os.path.join(root, file_name)
                
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()
                        prompts.append({
                            "file_name": file_name,
                            "type": "system_prompt",
                            "content": content,
                            "path": os.path.relpath(file_path, directory_path)
                        })
                except (UnicodeDecodeError, OSError):
                    continue
                    
    return prompts

def store_directory_content_in_json(directory_path, output_json_path):
    """
    Walk through a directory and subdirectories, extract both Python functions
    and system prompts, and store them in a single JSON file.
    
    :param directory_path: Path to the directory to search.
    :param output_json_path: Path to the JSON file where the extracted info will be saved.
    """
    results = {
        "functions": [],
        "system_prompts": []
    }

    # Get the absolute path of the current script
    current_script = os.path.abspath(__file__)
    
    # Collect Python functions
    for root, dirs, files in os.walk(directory_path):
        for file_name in files:
            if file_name.endswith(".py"):
                file_path = os.path.join(root, file_name)
                
                # Skip if this is the current script
                if os.path.abspath(file_path) == current_script:
                    continue

                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        file_content = f.read()
                except (UnicodeDecodeError, OSError):
                    continue

                try:
                    tree = ast.parse(file_content, filename=file_path)
                except SyntaxError:
                    continue

                for node in ast.walk(tree):
                    if isinstance(node, ast.FunctionDef):
                        function_source = ast.get_source_segment(file_content, node)
                        
                        results["functions"].append({
                            "file_name": file_name,
                            "type": "function",
                            "function_name": node.name,
                            "line_number": node.lineno,
                            "source": function_source,
                            "path": os.path.relpath(file_path, directory_path)
                        })

    # Collect system prompts
    results["system_prompts"] = read_system_prompts(directory_path)

    # Write results to JSON
    with open(output_json_path, "w", encoding="utf-8") as json_file:
        json.dump(results, json_file, indent=4)

    print(f"Extracted content saved to {output_json_path}")
    print(f"Found {len(results['functions'])} functions and {len(results['system_prompts'])} system prompts")

def main():
    directory_to_scan = os.getcwd()
    output_json_path = "content_metadata.json"
    store_directory_content_in_json(directory_to_scan, output_json_path)

if __name__ == "__main__":
    main()