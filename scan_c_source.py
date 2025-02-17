import os
import json
import argparse
import re
from datetime import datetime

import re

def strip_comments(source_code):
    """Remove C and C++ comments from source code while preserving string literals."""
    
    # Regular expression to match comments (single-line and multi-line)
    pattern = r'(\".*?\"|\'.*?\'|//.*?$|/\\*.*?\\*/)'
    
    def replacer(match):
        if match.group(0).startswith(("//", "/*")):
            return ""  # Remove comments
        return match.group(0)  # Keep strings intact
    
    regex = re.compile(pattern, re.DOTALL | re.MULTILINE)
    return regex.sub(replacer, source_code)

def scan_directory(directory, strip_comments_flag):
    """Scan directory recursively for C, C++, and header files."""
    source_files = []
    extensions = {'.c', '.cpp', '.cxx', '.cc', '.h', '.hpp', '.hxx'}
    
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(tuple(extensions)):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        source_code = f.read()
                    
                    if strip_comments_flag:
                        source_code = strip_comments(source_code)
                    
                    metadata = {
                        'file_path': file_path,
                        'file_name': file,
                        'last_modified': datetime.fromtimestamp(os.path.getmtime(file_path)).isoformat(),
                        'size_bytes': os.path.getsize(file_path),
                        'source_code': source_code
                    }
                    source_files.append(metadata)
                except Exception as e:
                    print(f"Skipping {file_path} due to error: {e}")
    
    return source_files

def split_and_save_json(data, output_file, max_size):
    """Split data into multiple JSON files if exceeding max_size (in KB)."""
    max_bytes = max_size * 1024  # Convert KB to bytes
    part = 1
    current_size = 0
    chunk = []
    
    for item in data:
        item_size = len(json.dumps(item, ensure_ascii=False).encode('utf-8'))
        if current_size + item_size > max_bytes and chunk:
            with open(f"{output_file}_part{part}.json", 'w', encoding='utf-8') as json_file:
                json.dump(chunk, json_file, indent=4)
            print(f"Saved: {output_file}_part{part}.json")
            part += 1
            chunk = []
            current_size = 0
        chunk.append(item)
        current_size += item_size
    
    if chunk:
        with open(f"{output_file}_part{part}.json", 'w', encoding='utf-8') as json_file:
            json.dump(chunk, json_file, indent=4)
        print(f"Saved: {output_file}_part{part}.json")

def main():
    parser = argparse.ArgumentParser(description="Scan and extract C/C++ source files into JSON files.")
    parser.add_argument('-o', '--output', type=str, default='source_files', help="Output JSON file name prefix.")
    parser.add_argument('--strip-comments', action='store_true', help="Strip comments from source files.")
    parser.add_argument('--max-size', type=int, default=5120, help="Maximum JSON file size in KB before splitting.")
    args = parser.parse_args()
    
    directory = os.getcwd()
    print(f"Scanning directory: {directory}")
    source_files = scan_directory(directory, args.strip_comments)
    
    split_and_save_json(source_files, args.output, args.max_size)

if __name__ == "__main__":
    main()
