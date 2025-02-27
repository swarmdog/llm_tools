
# XCOM 2-Inspired HexGen AI GM Rule System

This rule system adapts **HexGen RPG** mechanics to the tactical world of **XCOM 2**, providing a streamlined framework for an AI-driven Game Master. It combines HexGen’s **dice pool** resolution with XCOM’s turn-based combat and strategy layer. All rules are designed for straightforward **Python** implementation, enabling automation of dice rolls, turn logic, and AI decisions.

## 1. Core Mechanics: HexGen Dice Meets XCOM Tactics

- **Dice Pool Resolution**: Actions are resolved with HexGen’s dice pool system. Each skill or attack is rated in **d6 dice** (e.g. 4D6 means roll four six-sided dice). To succeed on a check, the total roll must meet or exceed a **Target Number (TN)**. Difficulty of tasks ranges from Mundane (TN ~5) up to Legendary (TN 40+), as per HexGen’s guidelines. For example, a normal shot might be TN 10–12, while a difficult long-range sniper shot could be TN 20+. The AI GM calculates the dice pool, rolls, and compares against TN to determine success or failure.

- **Success and Failure**: The degree by which the roll meets or falls short of the TN can matter. HexGen defines success margins: meeting TN exactly is a basic success, exceeding by +10 is an **Excellent** success, and +20 is a **Triumph**. In combat, these margins translate into effects like critical hits (see Combat section). Failing below TN can yield complications. This margin system allows the AI to narratively scale outcomes (e.g. a *Triumph* on a hacking attempt might grant bonus intel, while an *Epic Fail* could trigger an alarm).

- **Turn Structure**: The game runs in **turn-based rounds**. Each unit (soldier or enemy) typically gets **2 Actions per turn** (mirroring XCOM’s two-action system). Movement, shooting, reloading, or using an ability each cost one action (some heavy attacks or dashes use two). The AI GM manages initiative by alternating between player squad turns and enemy turns, similar to XCOM’s phase-based system. Within each phase, the order of individual unit actions can be flexible or predetermined, as long as each entity acts once. This structure is easy to automate: e.g., a Python loop iterates over units and executes their chosen actions each round.

- **Hexagonal Grid & Movement**: Battles take place on a hex-based grid (HexGen is hex-friendly). Each soldier and enemy has a **Mobility** stat determining how many hexes they can move per action. For example, 6 hexes for a standard move and up to 12 with a dash (using both actions). Terrain features like high ground or obstacles can modify movement costs (e.g., climbing a ledge costs extra). The AI can represent positions as coordinate pairs and handle movement by updating coordinates and checking distance. Pathfinding can be simplified by allowing straight-line movement up to the limit (since fine pathfinding is beyond scope of rules, a simple distance check suffices for a streamlined system).

- **Easy Automation**: All mechanics rely on numeric values (dice counts, target numbers, distances) with minimal GM judgment calls, which suits Python automation. Data structures can represent game entities (e.g. a `Soldier` class with attributes for skills, health, etc., and methods for actions). The AI GM uses functions for tasks like `roll_dice(pool)` or `move_unit(unit, target_hex)` to handle outcomes consistently. By keeping rules computational (dice math, comparisons), the AI can seamlessly manage encounters, track stats, and make decisions without human input.

## 2. Soldier System: Point-Buy Classes & Progression

- **Character Creation (Point-Buy)**: Soldiers are created using HexGen’s point-buy system. Each soldier begins with a pool of **Training Points (TP)** ([basicrules.pdf](file://file-CX78mpf2SobqfBf4A2ixVs#:~:text=You%20use%20Training%20Points%20,as%20you%20purchase%20new%20skills)) to spend on their background, skills, and special abilities. In HexGen, everything (skills, upgrades) costs 1 TP, making it simple to allocate in code. For example, a new soldier might get 5 TP: they spend 1 on a **Background/Class** and the rest on skills or perks. The AI GM can present class choices or even auto-generate soldiers by distributing points according to class templates.

- **XCOM Classes as Backgrounds**: The four primary XCOM 2 classes are implemented as HexGen-style backgrounds that define a soldier’s starting proficiencies:
  - **Ranger** – Infantry scout specializing in close combat. Starts with training in **Small Arms** (for shotguns) and **Martial Arts** (for sword attacks) as Primary Skills, reflecting close-range marksmanship and melee prowess. Rangers might also take **Covert Ops** as a Secondary Skill to represent stealth (e.g. Phantom ability). These skills begin at 4D6 if trained, giving a solid dice pool. For instance, a rookie Ranger could have Small Arms 4D6 and Martial Arts 4D6.
  - **Sharpshooter** – Sniper and pistol expert. Primary skill in **Small Arms** (focus on sniper rifles) and possibly a secondary in **Athletics** or a custom “Aim” attribute to steady aim. Sharpshooters often invest TP in abilities like Squad Sight (treat distant targets as within range) or pistol training. Their high skill dice reflect excellent marksmanship. A veteran Sharpshooter might reach 6D6 or higher in Small Arms, corresponding to expert proficiency.
  - **Grenadier** – Demolition and heavy weapons trooper. Uses **Heavy Weapons** skill as Primary (covering machine guns/cannons and grenade launchers). Secondary skills could include **Mechanics** or **Explosives** for handling grenades and heavy armor. Grenadiers might spend points on upgrades like *Blast Padding* (extra armor) or improved grenade range. Their point-buy choices reflect becoming a heavy ordnance specialist.
  - **Specialist** – Tech and support class. Primary skill in **Hacking/Tech** (using HexGen’s **Software** or **Process** skill as an analog for the GREMLIN drone hacking), and a secondary in **Medicine** (for the medikit protocol). Specialists often purchase the **Medical Protocol** ability (remote heal) and **Combat Protocol** (combat drone attack) as character upgrades. Their skills ensure decent dice pools for hacking challenges and healing tasks.

  Each class background might grant a starting equipment package and a special perk (e.g., Rangers begin missions **concealed** via a “Phantom” perk). Under the hood, these are just effects the AI applies (concealment status = true) rather than extra rules complexity.

- **Attributes and Skills**: Instead of traditional RPG attributes (Strength, Agility, etc.), this system emphasizes skills that map to combat performance:
  - **Aim** and weapon proficiency are embodied by the relevant combat skill’s dice pool (e.g., a soldier’s Small Arms skill determines their shooting accuracy).
  - **Mobility** is an attribute (measured in hexes per move). Rangers and Sharpshooters might have base 10, Grenadiers slightly less (due to heavy gear), Specialists average.
  - **Health** is standardized (XCOM soldiers typically have low single-digit HP, but in HexGen scale we use higher values). By default, use HexGen’s base Health of **20** for an unarmored human. Each point of damage reduces Health; reaching 0 means the soldier is down or killed.
  - **Will** or mental fortitude can be represented by a **Cool** or **Presence** skill (if using HexGen’s skill list) or a simple Will attribute for resisting panic/psi attacks.
  - **Armor** stat uses HexGen’s armor dice: e.g., basic Kevlar armor might give **1D6 armor** (rolled to reduce incoming damage), heavier armor 2D6 or more. This way, armor absorbs some damage when soldiers are hit, akin to XCOM’s ablative armor points.

  These values are easy to store in a Python object. For example:
  ```python
  class Soldier:
      def __init__(self, name, cls):
          self.name = name
          self.class_name = cls
          self.health = 20
          self.skills = {'Small Arms': 3, 'Heavy Weapons': 0, 'Tech': 0, ...}  # values represent number of D6 beyond base 3D6
          self.armor_dice = 1  # 1D6 armor
          # etc.
  ```
  Here a skill value of 3 means 6D6 pool (base 3D6 untrained +3D6 from training/upgrades, since untrained = 3D6). The AI can calculate the dice pool as `base 3 + skill_value` dice.

- **Progression**: Soldiers earn experience from missions. Instead of discrete levels, they gain additional **Training Points** which the AI GM can spend to improve skills or buy new abilities. For example, after a mission, a soldier might get 1 TP to spend – the AI could automatically upgrade their primary skill (increasing its dice by +1D6 every two upgrades) or unlock a class ability. This mimics XCOM’s promotion system: e.g., after a few missions a Ranger unlocks “Run and Gun” by spending a TP, granting them a once-per-mission ability to dash and still shoot. Since each upgrade costs 1 TP ([basicrules.pdf](file://file-CX78mpf2SobqfBf4A2ixVs#:~:text=You%20use%20Training%20Points%20,as%20you%20purchase%20new%20skills)), tracking and spending them in code is straightforward. The AI ensures soldiers remain within **Tier** limits (HexGen caps skill dice based on campaign tier, e.g. Tier 1 max 6D6 for primaries).

- **Skill Checks Beyond Combat**: For base management or geoscape actions (research, engineering, etc.), soldiers or staff can use the same skill system. For instance, a scientist’s **Research** could be treated as a skill check with difficulty based on project complexity. A hacking attempt in a mission uses the Specialist’s Tech skill vs. a target TN (the door’s security level). This unified mechanic means the AI can use one function `skill_check(character, skill, TN)` for everything: combat shots, hacking objectives, or strategy tasks. 

## 3. Turn-Based Combat System

Combat follows XCOM 2’s tactical style, implemented with HexGen’s action resolution. Each turn, the AI Game Master processes movements, cover, attacks, and abilities for both sides. Key rules include:

- **Initiative and Rounds**: Battles proceed in rounds where the **XCOM squad acts, then the enemy** (or vice versa, depending on surprise). During the XCOM phase, players can activate soldiers in any order. The AI GM can either preserve a fixed sequence or dynamically choose an optimal order (e.g., soldiers in better positions act first). In the enemy phase, the AI controls all aliens. This alternating phase structure simplifies coordination and is easy to implement (loop through all soldiers for actions, then all enemies).

- **Actions and Movement**: Each unit has **2 Actions**. Common actions (costing 1 action each) include: Move (up to mobility range), Shoot, Reload, Overwatch, Hide (if class ability allows re-concealment), use Ability or Item. Certain heavy actions cost 2 actions (e.g. dash = move double distance, some special attacks like a sniper’s aim-shoot ability or firing a heavy weapon after moving might require both actions). For automation, each unit can have a simple action counter. For example:
  ```python
  for unit in squad:
      actions = 2
      if need_to_move:
          move_unit(unit, dest)
          actions -= 2 if dashing else 1
      if actions > 0:
          execute_attack(unit, target)
  ```
  The AI decides whether to use one action to move and one to shoot, or both to dash, etc., based on goals and available enemies.

- **Cover System**: Taking cover is crucial. Cover in this system gives a **defensive bonus** by imposing a penalty on attackers’ shots, much like XCOM’s defense stat. In practice:
  - **Half cover** (low cover, like a crate or half-wall) imposes a *-1D6 penalty* on incoming shots (the attacker rolls one fewer die) – this reflects roughly +20 Defense.
  - **Full cover** (high cover, like a tall wall) imposes *-2D6 penalty* on shots (attacker rolls two fewer dice), reflecting ~+40 Defense.
  - These penalties align with HexGen’s notion of unfavorable conditions: *-1D6 for a normal hindrance, -2D6 for severe*. The AI GM checks line-of-sight and cover for each attack: if the target is in cover relative to the shooter’s position, it applies the appropriate dice reduction. For instance, if a Sectoid fires at a soldier in full cover, and the Sectoid’s base pool is 4D6, the AI will roll 2D6 (4-2) for the attack.
  - **Flanking**: If a unit moves to a flank such that the target’s cover does not protect against that angle, the target is effectively in the open. A flanked target grants **no cover penalty** to the attacker and even makes them vulnerable to critical hits. XCOM grants +50% crit chance when an enemy is out of cover. In our system, flanking can provide an **Edge die** (+1D6 bonus) to the attacker to represent the increased lethality of an exposed shot. The AI will prioritize flanking maneuvers for both soldiers and intelligent enemies to gain this advantage.

- **Shooting and Hit Resolution**: When a unit fires a weapon, resolve it as a skill check:
  - Each weapon has a **Handling rating** (TN to hit at optimal range) based on HexGen stats. For example, an assault rifle might have TN 14 for a medium-range shot. The shooter rolls their relevant skill dice pool (e.g. Small Arms 5D6 for a trained squaddie) against this TN. The AI calculates modifiers: target’s cover (dice penalty as above), shooter’s status (e.g. -1D6 if they moved and are using a sniper rifle that penalizes movement, or +1D6 if using a perfect height advantage).
  - If the sum of the dice ≥ TN, the shot **hits**. If below, it **misses**. For simplicity, we do not calculate separate hit percentages – the dice roll inherently produces success/failure. However, the AI can translate the result into a percentage for user display if needed (since dice probabilities are known, but it’s simpler to just narrate the outcome).
  - **Critical Hits**: If the attack roll exceeds the TN by a certain margin (e.g. ≥ TN + 10), treat it as a **critical hit**. A critical hit inflicts extra damage. In HexGen ballistic rules, beating TN by 10 could mean an extra bullet hits; in XCOM terms, we can implement crits as +50% damage or an extra damage die. For example, an assault rifle that normally does 2D12 damage might do 3D12 on a crit. The AI checks the roll margin and applies these effects automatically. (Conversely, if a roll is far below TN, the AI might describe a “graze” or complete miss, though for simplicity a miss is just a miss in mechanics).
  - **Damage Resolution**: Each weapon has a damage roll (dice) associated. XCOM uses fixed ranges, but HexGen uses dice, which we’ll adopt for consistency. For instance, a conventional Assault Rifle might deal **2D6** or **2D8** damage; a Shotgun might deal **3D6** at close range but with a higher TN for distance. The AI rolls damage dice on a hit and then subtracts any armor. If a soldier has Body Armor 2D6, the AI would roll that and subtract the result from damage (this mirrors XCOM’s armor reducing damage). Any remaining damage is subtracted from Health. All these calculations are straightforward arithmetic for the AI GM to handle.

- **Abilities and Special Actions**: Soldiers and aliens can perform unique actions:
  - **Overwatch**: A soldier can spend their action to overwatch, meaning during the enemy turn, if any visible enemy moves, the soldier gets a free reaction shot. The AI handles this by flagging the soldier as “on overwatch” and checking triggers during enemy movement. Overwatch shots are resolved like normal attacks (perhaps with a small aim penalty as in XCOM). Enemies can also use overwatch if their AI behavior allows.
  - **Grenades and AoE**: Using a grenade is a one-action attack that affects an area. Grenades don’t require an accuracy roll in XCOM (they automatically hit the area), so we can say they automatically hit all targets in the blast radius in our system too. The AI will roll damage for each target (e.g. a Frag Grenade might do 3D6 damage to everyone in a 2-hex radius). Grenades also destroy cover objects. The AI can model cover as having hit points; a grenade hit simply removes the cover in its radius. This is easy to simulate by flagging those map cells as now open. (HexGen’s rules note that explosions deal full damage to everyone in area, which we follow).
  - **Melee Attacks**: Rangers (with swords) or certain aliens (Chryssalids, Mutons) use melee. A melee attack is resolved as a skill check (Martial Arts or melee skill) against the target’s melee defense (we can use a standard TN or opposed roll). Typically, melee in XCOM hits more reliably. We might set a base TN (like 10 for melee if target is adjacent), modified by things like defense or dodge. On a hit, melee damage (e.g. Ranger sword 4D6) is applied. Melee can also crit by the same margin rule. The AI will favor melee attacks for units like Chryssalids who are built for it, closing distance and attacking in one turn if possible (Chryssalids are allowed to attack after dashing in XCOM).
  - **Critical Mechanics**: Besides hit roll crits, certain class abilities or circumstances ensure criticals. For example, the Rangers’ **Blademaster** ability might simply add +2 damage rather than modifying dice, but **Hunter’s Instincts** (bonus damage on flanked enemies) effectively triggers on flanking shots. The AI can incorporate these by adjusting damage or dice when those conditions are met. This keeps the core resolution the same, just with tweaked inputs.

- **Line of Sight and Range**: The AI GM checks if a shooter has line of sight to a target (no solid obstacles in a straight line hex path). If using a grid, we can define simple rules: e.g., an obstacle blocks LoS if neither the shooter nor target is adjacent to it (to allow peeking from cover edges). Range can affect TN or dice: weapons might have optimal range and suffer penalties beyond it. For simplicity, we can say:
  - If target is within a weapon’s **effective range**, use its normal TN. If beyond, increase TN (or give attacker -1D6) for long range. For example, a sniper rifle might have no penalty at long range (due to Squad Sight ability), whereas a shotgun beyond 5 hexes might incur -2D6. These can be encoded as weapon properties and checked by the AI.
  - Close-range bonus: conversely, some weapons (shotguns, swords) might get a bonus when very close. The AI can grant +1D6 if a shotgun is within 2 hexes, for instance.
  - These range modifiers ensure that positioning matters. The AI will use them to decide tactics (e.g. a Sharpshooter will often stay back, but a Ranger will try to rush within sword range if safe).

In summary, the combat system provides a turn-based loop of movement, cover, and attack decisions. It leverages HexGen’s dice for uncertainty, while mirroring XCOM’s rules for cover (+Defense) and actions. The AI can simulate this reliably by following the above rules each turn, making it predictable to code yet rich enough to feel like XCOM.

## 4. Equipment and Abilities Integration

XCOM 2 features a variety of weapons, armors, and special abilities. We integrate these into the HexGen framework so that equipment modifies dice rolls and abilities are extensions of the action system. All equipment and powers are data-driven, which the AI can easily manage.

- **Weapon Types**: We include the full range of XCOM 2 weapons, each defined by:
  - **Type and Skill**: What skill is used to fire it (for soldiers, usually Small Arms for rifles/pistols, Heavy Weapons for cannons, etc.). This links to the soldier’s dice pool.
  - **Handling (TN)**: The base Target Number to hit at optimal range. For example, an **Assault Rifle** might have TN 12 for short range, increasing at longer range; a **Sniper Rifle** might have TN 15 if fired after moving (higher if the shooter moved, to reflect aim penalty) or TN 10 if the shooter is stationary and using a scope (to reflect aim bonuses).
  - **Damage**: The damage roll (dice) on a hit. We can set these to mimic XCOM’s average damage. Examples:
    - Assault Rifle: 2D8 damage (approx ~9 average, similar to 3-5 in XCOM2 early game).
    - Shotgun: 3D6 damage (~10 average) at close range, but if target beyond a few hexes, the TN increases significantly (or damage dice reduce) to model falloff.
    - Sniper Rifle: 2D10 damage (~11 avg) for conventional sniper, high crit potential.
    - Cannon (heavy machine gun): 2D8 damage like AR but also **Shred 1** (if a weapon has a **Shred** property, it means it removes that many armor dice from the target on hit, as Muton rifles do ([Muton (XCOM 2) | XCOM Wiki | Fandom](https://xcom.fandom.com/wiki/Muton_(XCOM_2)#:~:text=Beam%20Rifle%3A))). The AI will reduce the target’s armor rating accordingly on a hit.
    - Pistol: 1D8 damage (~4-5 avg), used by Sharpshooters for quick shots.
    - Sword (Ranger melee weapon): 3D6 damage, ignores target’s cover (since it’s melee), and on a crit might do an extra 1D6 bleed.
    - Grenade Launcher (used by Grenadiers to launch grenades farther): effectively extends grenade range and could increase grenade blast radius slightly. The “to hit” is usually automatic for grenades in radius.
    - Heavy Weapons (ex: rocket launcher, flamethrower from EXO suits): these are special gear items that cause area damage or effects. A rocket might do 4D6 in a radius and destroy cover. They might be limited-use (one per mission). The AI treats them as abilities rather than normal attacks.

  All these weapons can be stored in a Python dictionary, e.g. `weapons = {"Assault Rifle": {"skill":"Small Arms", "TN":12, "damage":"2d8", "shred":0, ...}, ...}`. When a soldier attacks, the AI references their equipped weapon’s data to know how to resolve it.

- **Armor and Gear**: Armor provides defensive dice:
  - **Kevlar Armor** (starting gear): 0 or 1D6 armor (light protection). Health remains 20.
  - **Plated Armor** (mid-tier, e.g. Predator armor): 2D6 armor, and maybe +5 Health bonus. This is akin to providing some ablative padding.
  - **Powered Armor** (late-tier, e.g. Warden armor): 3D6 or more armor, +10 Health.
  - Armor can also confer item slots or special abilities (e.g., EXO suit allows use of a Rocket Launcher once). Those can be handled as granting the soldier an extra “weapon/ability”.
  - **Utility Items**: This includes medikits, ammo upgrades, etc. Medikits allow a **Heal** action (restoring, say, 10 Health or a roll like 2D6 healing). Skulljack (a special item) allows using the Hack skill in melee to trigger story events. Ammo like **Talon Rounds** could simply grant +1D6 on crit damage for that soldier’s shots. The AI can keep track of these item effects as modifiers when relevant (for instance, if soldier.has_item("Talon Rounds"): increase crit damage).

- **Soldier Abilities**: We integrate XCOM 2 class abilities as HexGen **Character Upgrades** (purchased with Training Points). They function as conditional modifiers or extra action options. Some key examples:
  - **Run & Gun** (Ranger ability): Allows the soldier to take an action after dashing. Implementation: if ability is available and the Ranger dashes (uses both actions to move), the AI GM grants a bonus action to use for an attack. This can be limited to once per mission (track a cooldown or use_count).
  - **Phantom** (Ranger ability): Soldier remains concealed when the squad is revealed. Implementation: a boolean flag on the soldier at mission start that prevents them from being revealed until they attack. The AI would exclude Phantom Rangers from enemy targeting until they break concealment.
  - **Blademaster** (Ranger ability): +2 damage on sword attacks. Implementation: simply add 2 to sword damage rolls (or treat as +1D6 for an average of +3.5 damage for more dice flavor).
  - **Squadsight** (Sharpshooter passive): Can shoot targets that allies see at long range. Implementation: remove range penalties for sniper rifle and allow targeting enemies not in direct line-of-sight if an ally has LoS. The AI can check if any soldier sees an enemy, then allow the sniper to shoot with an increased TN (for very long range) instead of forbidding the shot.
  - **Deadeye** (Sharpshooter ability): Take a shot with -1D6 to hit (less accuracy) but +1D6 damage. The AI can treat this as a toggle on a sniper shot action: if used, apply the dice adjustments accordingly.
  - **Lightning Hands** (Sharpshooter pistols): A free pistol shot (no action cost, once per few turns). Implementation: allow an extra pistol attack action for the sharpshooter when triggered, with an internal cooldown.
  - **Hail of Bullets** (Grenadier ability): A shot that **automatically hits** but uses lots of ammo. Implementation: skip the accuracy roll (treat as hit) but perhaps impose a penalty like needing a reload afterward. Automatic hit is easy: the AI just applies damage without a roll, which in HexGen terms is like having a TN of 0 so it always succeeds.
  - **Shredder** (Grenadier passive): Bullets shred armor. Implementation: mark all primary weapon attacks from this soldier as `shred: 1` (removing one armor die from targets on hit).
  - **Medical Protocol** (Specialist ability): Send GREMLIN to heal an ally remotely. Implementation: a Heal action that doesn’t require the Specialist to move to the target, range limited by GREMLIN distance (say 20 hexes). The AI uses this when a soldier is wounded and the Specialist has a medkit.
  - **Combat Protocol** (Specialist ability): Guaranteed damage to robotic enemy via GREMLIN shock. Implementation: similar to Hail of Bullets, it auto-hits a mechanical target for fixed damage (e.g. 4D6) ignoring armor. Useable once or twice per mission per Specialist.
  - **Hack** (Specialist action): Use GREMLIN to hack an objective or enemy robot. This is a skill check using Tech skill vs a target TN (based on enemy’s defense or device’s security). For instance, hacking an ADVENT turret might be TN 15. On success, the turret is shut down or converted. The AI handles this via the normal dice roll and then changes the state of the target (e.g., mark turret as allied or inactive).
  - **Aid Protocol**: Grant an ally +1D6 defense (or effectively give them high cover bonus even in open) for a turn by the GREMLIN. Implementation: toggle a status on the target that increases cover level for one enemy turn. The AI would then apply an extra -1D6 to any attacks against that protected ally.

  Each ability has a clear trigger and effect, which are easy to encode. The AI can maintain a list of abilities for each soldier with flags like `cooldown` or `uses` to enforce limitations. When an ability is used, the AI prints a message (e.g. "Specialist uses Aid Protocol on Ranger, granting bonus defense") and adjusts the relevant stats for the duration.

- **Enemy Abilities**: Enemy types also have abilities that the AI GM will use (detailed in the Enemy section). For instance, Sectoids have **Psi abilities** (Mindspin, reanimate), Mutons have **Suppression** and **Counterattack**, Vipers have **Bind**, etc. These are implemented similarly: as actions with certain effects (Mindspin forces a Will save for the soldier or they panic/get controlled). By treating them as abilities in the same framework, the AI can manage enemy actions uniformly.

- **Base Management Equipment**: Outside of missions, the XCOM base (the Avenger) has facilities that yield upgrades (e.g. new armor or weapons). For the rule system, we abstract this: research projects unlock new tiers of equipment which simply become new entries in the equipment lists (replacing or upgrading old ones). The AI can handle base research as a between-mission phase where, given a research choice, it “unlocks” an item after X days (maybe skip actual time tracking in favor of mission count). Because the question focuses on missions, we won’t elaborate deeply, but the point is the rules support adding improved gear and abilities seamlessly. A simple tech tree can be encoded as prerequisites: e.g., Research “Plated Armor” -> unlock Predator Armor item with better stats; Research “Gauss Weapons” -> upgrade sniper and cannon damage values, etc.

In summary, all XCOM equipment and abilities are translated into modifiers of the core dice mechanics or new actions with defined outcomes. This makes them amenable to automation: the AI just needs to check conditions (like “ability available?” or “target in range?”) and then apply the pre-defined effect.

## 5. Enemy System: Stat Blocks and AI Behavior

The enemies in XCOM 2 are represented with HexGen-style stat blocks and programmed behaviors. Each enemy type has a template defining its attributes (health, armor, skills, weapons) and AI tactics. The AI Game Master uses these to simulate enemy actions in a believable way.

- **Stat Block Structure**: An enemy’s stat block includes:
  - **Health**: How much damage it can take (often higher than a basic soldier for mid-tier aliens). For example, a **Sectoid** might have ~8 Health in XCOM (which in our system we’ll scale to ~15 or 20 to account for our damage scale), a **Muton** might have ~11 (scaled to ~25). Boss enemies (e.g. Sectopod) have much more.
  - **Armor**: Armor dice reducing damage. Early-game aliens like Sectoids and basic ADVENT have 0 armor, mid-tier like Mutons have 1D6 armor (since Mutons have 1 point armor in XCOM2 ([Muton (XCOM 2) | XCOM Wiki | Fandom](https://xcom.fandom.com/wiki/Muton_(XCOM_2)#:~:text=Armor))), heavy units like Andromedons might have 2D6.
  - **Defense**: Base defense (evasion) that effectively raises the TN to hit them. For instance, a Muton has 10 Defense ([Muton (XCOM 2) | XCOM Wiki | Fandom](https://xcom.fandom.com/wiki/Muton_(XCOM_2)#:~:text=Defense)). We model this by giving attackers a penalty of -1D6 or adding +3 to the TN when shooting at a Muton. Most basic enemies have 0 defense (no penalty).
  - **Mobility**: How many hexes they move per action. A Sectoid moves ~12 hexes (they are relatively quick), a Muton around 12-14 ([Muton (XCOM 2) | XCOM Wiki | Fandom](https://xcom.fandom.com/wiki/Muton_(XCOM_2)#:~:text=Mobility)), a Chryssalid very high (~15+). The AI uses this to decide how far an enemy can go when chasing or flanking.
  - **Aim/Skills**: Instead of a raw Aim percentage, enemies have a dice pool for attacks. This can be derived from their aim stat (e.g., Sectoid Aim 70 implies a moderate skill, say 4D6 pool for its pistol; Muton Aim ~75-80 => maybe 5D6 pool for its rifle). We assign skills similar to soldiers:
    - Ranged combat skill for their weapon (Small Arms for many aliens, Heavy Weapons for ones using heavy guns).
    - Melee skill if they have melee attacks (Muton bayonet, Chryssalid claws).
    - Psi skill for psionics (Sectoid’s psi ability might be a 5D6 or 6D6 vs the soldier’s Will TN).
  - **Weapon and Damage**: The weapon they use and its damage dice. This is often the alien’s natural attack:
    - **ADVENT Trooper**: Standard rifle, comparable to XCOM assault rifle (TN ~12, damage 2D6).
    - **ADVENT Officer**: Similar rifle, plus a **Mark Target** ability (which we’ll implement as granting bonus to other enemies’ aim against that target).
    - **Sectoid**: Carries a pistol (3-4 damage in XCOM ([Sectoid (XCOM 2) | XCOM Wiki | Fandom](https://xcom.fandom.com/wiki/Sectoid_(XCOM_2)#:~:text=Beam%20Pistol%3A%203,critical%20damage)), so maybe 1D8+1 damage here) – not very lethal with guns, but has strong Psi attacks.
    - **Muton**: Has a plasma rifle (4-6 damage ([Muton (XCOM 2) | XCOM Wiki | Fandom](https://xcom.fandom.com/wiki/Muton_(XCOM_2)#:~:text=Beam%20Rifle%3A)), we model as 2D8+1 maybe) that shreds armor, a melee bayonet (6-8 damage ([Muton (XCOM 2) | XCOM Wiki | Fandom](https://xcom.fandom.com/wiki/Muton_(XCOM_2)#:~:text=Bayonet%3A)), treat as 2D6+2dmg with a chance to stun), and a grenade (4-5 damage area ([Muton (XCOM 2) | XCOM Wiki | Fandom](https://xcom.fandom.com/wiki/Muton_(XCOM_2)#:~:text=Plasma%20Grenade%3A))).
    - **Chryssalid**: Only melee claws, but very dangerous: say 3D6 damage and causes **Poison** (ongoing damage or penalty to the soldier). It also has the ability to **burrow** (become hidden under the ground).
    - **Viper**: Plasma rifle (like 3-5 damage), plus **Tongue Pull** (range attack to pull a soldier) and **Bind** (essentially a melee grapple that immobilizes and damages each turn). These would be abilities in its profile.
    - **Other enemies**: We can similarly define Archons (flying melee/fire attackers), Andromedons (heavy armor and acid), Sectopods (huge walkers with high damage), etc., but the mission may not include all. The system is extensible.

  For example, a **Sectoid stat block** in notation might look like: 
  ```
  Sectoid:
    Health: 15   Armor: 0   Defense: 0   Mobility: 12
    Skills: Small Arms 3 (roll 6D6 to shoot), Psi 4 (roll 7D6 for psi attacks)
    Weapon: Plasma Pistol (TN 10, Damage 1D8+1)
    Abilities: Mindspin (psi attack vs soldier Will), Psi Reanimate (revive a corpse as zombie)
  ```
  The AI uses this to decide how a Sectoid behaves (primarily using Psi). 

- **AI Behavior Patterns**: Each enemy type has a simple behavior script guiding its decisions, which the AI GM follows:
  - **ADVENT Troopers/Officers**: Basic infantry tactics. They will take cover and shoot at the closest or most exposed XCOM soldier. Officers will use **Mark Target** (ability that gives a specific XCOM unit -1D6 defense for a turn) at the start of engagement, then shoot. If flanked or alone, they might fall back to better cover. These are straightforward to automate: evaluate cover positions and line-of-sight to decide move, then either use ability or fire.
  - **Sectoid**: Prefers psi attacks. Behavior: If any XCOM soldier is not currently mind-controlled or panicked, the Sectoid will use **Mindspin** (an ability that can cause panic, disorientation, or mind control ([Sectoid (XCOM 2) | XCOM Wiki | Fandom](https://xcom.fandom.com/wiki/Sectoid_(XCOM_2)#:~:text=,from%20the%20corpse%20of%20a))). The AI resolves Mindspin as a psi skill check (Sectoid’s Psi 7D6 vs a TN equal to the soldier’s Will or a fixed difficulty). On success, it inflicts a status: possibly panic (soldier loses next turn), or even mind control (the AI temporarily adds the soldier to the alien team for a few turns). If the Sectoid is alone or has already used psi this turn, it may shoot its pistol as a secondary option. Sectoids tend to stay back, using their 12 mobility to keep distance. If a zombie is available (via Psi Reanimate), the Sectoid might use that on a corpse instead of mind-controlling.
  - **Muton**: Aggressive mid-range combatant. Behavior: A Muton will move into medium range and fire its plasma rifle, especially using **Suppression** if a soldier is in heavy cover (Suppression in XCOM imposes -Aim on the target and grants a reaction shot ([Muton (XCOM 2) | XCOM Wiki | Fandom](https://xcom.fandom.com/wiki/Muton_(XCOM_2)#:~:text=,hitting%20them%20with%20their%20Bayonet)); in our system, we can say the Muton spends both actions to suppress, giving the targeted soldier -2D6 on their next attack and if that soldier moves, the Muton gets a free shot). If a soldier gets close, the Muton happily uses its **Bayonet** melee attack instead (which can stun on a hit ([Muton (XCOM 2) | XCOM Wiki | Fandom](https://xcom.fandom.com/wiki/Muton_(XCOM_2)#:~:text=ammuntion.%20,will%20trigger%20this%20as%20well))). The AI will check distance: if an XCOM soldier is within, say, 1 move distance, the Muton might charge and melee (because Mutons “take all opportunities to use the Bayonet” ([Muton (XCOM 2) | XCOM Wiki | Fandom](https://xcom.fandom.com/wiki/Muton_(XCOM_2)#:~:text=,One%20charge))). Mutons also carry a grenade: if two or more soldiers are clumped in cover, the Muton may throw a **Plasma Grenade** to hit them all and destroy their cover. This decision tree (if grouped target -> grenade; else if close -> melee; else if target in cover -> possibly suppress; else shoot) covers most Muton behavior. Mutons also have a **Counterattack** passive (they may retaliate against melee attacks) which the AI can implement as: if a soldier melees the Muton and the Muton is still alive, roll a chance (maybe 50%) to immediately perform a free bayonet attack back at the attacker.
  - **Chryssalid**: Fierce melee ambusher. Behavior: If not yet revealed, Chryssalids start **burrowed** (hidden). The AI keeps them immobile and undetectable until a soldier comes within a certain range or a timed trigger. When they strike, they will dash out (they can move very far) and claw the nearest soldier. A Chryssalid will always use both actions to either double-move into range and attack, or move and attack if already close. They do not use cover (they rely on not being seen and on causing chaos). After attacking, they might attempt to move back into cover or re-burrow if possible (in XCOM2 they can re-burrow after attacking). If a Chryssalid’s attack kills a target (especially a civilian or unattended NPC), the AI might spawn a **Chryssalid cocoon** (but for simplicity this can be omitted or be a mission-specific event). The important part is their AI is basically “hide, then jump and stab the closest target, causing poison.” Poison can be implemented as a status that deals a small damage (e.g. 2 HP) at the start of the soldier’s turns for a few rounds until cured by a medkit. The AI will track status effects like poison in the unit’s state and apply the damage automatically.
  - **Viper**: Cunning ranged and melee hybrid. Behavior: A Viper often tries a **Tongue Pull** as opening: a ranged ability to yank a soldier out of cover and right next to the Viper. If that succeeds, the Viper will use **Bind** (wrap up the soldier, immobilizing and dealing automatic melee damage each turn). The AI handles Tongue Pull as a skill check (maybe treat as an aimed ability with moderate TN). On success, move the soldier’s token adjacent to the Viper and mark them as bound (unable to act, taking e.g. 2D4 damage per turn until freed). Other soldiers can free the bound unit by killing the Viper or doing enough damage to it. If Tongue Pull is on cooldown or not ideal, the Viper will shoot its plasma rifle from cover, and if a soldier is 1 move away, it might slither forward and strike in melee. Vipers also have poison spit (small AoE causing poison status), which the AI may use if multiple XCOM are grouped behind cover (similar decision as a Muton grenade, but with poison effect).
  - **Other Enemies**: Each would have its own logic:
    - *Berserker*: no ranged attack, so just charges the nearest and punches.
    - *Andromedon*: uses acid bomb if multiple targets, otherwise shoots, and in second phase (after “death”) just charges melee.
    - *Sectopod*: will use big area attacks if multiple targets (Lightning Field, e.g.), or its main cannon on single targets. It may also stomp cover. It basically doesn’t use cover itself due to size.
    - *Turrets*: stationary, just shoot at best target with high aim.
    - These can be added as needed, following the pattern of checking conditions (distance, number of targets clumped, etc.) to pick an optimal action.

  The enemy behaviors are implemented as simple conditional routines that the AI GM follows each enemy turn. Because each enemy is fairly single-minded (they don’t coordinate beyond target prioritization), this is computationally simple. The AI can prioritize targets by some heuristic (e.g., attack the closest soldier, or the soldier with lowest health, or in XCOM often focus the player’s troops that are flanked or out of cover).

- **Example Enemy Turn**: On an enemy turn, the AI might do:
  1. For each active enemy, decide action:
     - Sectoid: picks a soldier not mind-controlled -> uses Mindspin.
     - Advent Troopers: find nearest soldier -> shoot (move into cover if not in cover already).
     - Muton: sees two soldiers behind same low wall -> throws grenade at them (destroying the wall).
     - Chryssalid: is burrowed -> a soldier came close, so it pops up and attacks that soldier.
  2. Execute those actions in some order (perhaps pod by pod). Use the dice mechanics to resolve each (except abilities that auto-hit).
  3. Apply results (damage, status effects).
  The AI ensures the actions make logical sense (e.g., not grenade if it would hit their own allies unless aliens are immune or desperate).

- **Difficulty Tuning**: Because this is AI-run, difficulty can be tuned by adjusting the enemies’ aim (dice pool) or health. For example, on an easier mode, the AI could treat all alien skill pools as one less D6, or give the XCOM soldiers an extra armor die. This way the framework can scale challenge without changing core rules. The mission generator (next section) can also alter the number of enemies to adjust difficulty.

By defining enemies in this structured way, the AI GM has all the info needed to manage them: stat blocks feed into the same combat resolution system, and behavior scripts guide their choices. This modular design makes it easy in Python to add new enemy types – just add a new stat dictionary and decision function, and the rest of the system (movement, shooting) works out-of-the-box.

## 6. Mission AI: Procedural Generation and Dynamic Encounters

The **Mission AI** is responsible for creating missions and guiding the flow of battle as a Game Master. It sets up objectives, terrain, enemy placement, and handles dynamic events (like reinforcements or alarms), making each mission feel unique. Key components:

- **Mission Structure**: Missions are generated with a specific **objective** and parameters:
  - Possible objectives include **Search & Destroy** (eliminate all enemies), **VIP Rescue or Escort**, **Sabotage** (plant X4 charges on a device), **Retrieval** (secure an item), or **Defense** (hold out against waves). The AI picks an objective based on campaign progression or at random.
  - Each objective comes with win/lose conditions that the AI checks (e.g., for Rescue: mission success if VIP unit reaches extraction zone, failure if VIP dies or turn limit exceeded).
  - The mission may have a turn limit or other pressures (e.g., a ticking clock until a device explodes or until reinforcements arrive).

- **Map Generation**: The battlefield is represented on a hex grid. The Mission AI can generate a map layout either randomly or from a set of predefined templates:
  - Terrain features like buildings, streets, forests, etc., can be placed. For Python implementation, a 2D array or similar structure can represent each cell (with markers for cover type: high, low, or no cover). For instance, a tree might provide low cover, a building wall high cover.
  - The AI can ensure some high cover and low cover is scattered so both sides have positions to use. It may mark certain zones as objective locations (e.g., a room where the VIP is held).
  - If fully procedural, this could be as simple as a grid with random obstacles. Alternatively, a small set of fixed maps (constructed as matrices) can be stored and the AI picks one matching the mission type.

- **Enemy Placement (Pods)**: Enemies are arranged typically in “pods” (groups) like in XCOM. The AI places a few pods across the map:
  - Each pod has 2-4 aliens depending on difficulty. For example, one pod might be 3 Advent Troopers led by an Officer; another pod a Sectoid with 2 Troopers; another a single Muton with a Viper; and possibly a Chryssalid pod hidden.
  - The pods can be assigned patrol routes. Initially, if XCOM is concealed, enemies wander. The AI can implement patrol by shifting the pod’s center a few hexes each turn within a region.
  - Enemies generally start unaware of XCOM’s presence. The mission AI keeps them in an “idle” state (patrolling or guarding) until **activated** (when they spot the XCOM squad or hear a loud explosion). This mimics the surprise element in XCOM missions.
  - When generating, the AI ensures pods are spaced out so the player doesn’t fight all at once (unless they trigger multiple pods). This can be done by quadrant: one pod in north area, one in south, etc.
  - If the mission is defense or terror-like (retaliation), enemies might continuously spawn from edges – the AI can schedule reinforcement pods on certain turn numbers or triggered by alarms.

- **Fog of War and Detection**: XCOM starts most missions in **concealment** (not initially seen by enemies). The AI tracks which soldiers are concealed. If a concealed soldier is in an enemy’s sight range and not in cover or flanking them, they might still remain hidden until they attack or move too close. We can simplify detection: each enemy has a vision radius (say 10 hexes). If a soldier is within that and in line-of-sight *and* not behind cover relative to that enemy (i.e., would be flanked if the enemy knew they were there), the enemy detects them. Otherwise, they remain hidden. Once any soldier is detected or an attack is made, the whole squad loses concealment (except those with special Phantom ability). The AI will handle this by checking at the end of XCOM’s turn if any enemies have line-of-sight to a soldier who isn’t explicitly in cover relative to them.
  - When concealment breaks or an engagement starts, the AI triggers enemy pods to **activate**: enemies shout and take cover or reposition immediately (perhaps they get a free scatter move upon activation as in XCOM). This can be implemented by giving each enemy out of cover a one-time movement into cover when activated before the player’s next action.
  
- **Dynamic AI Decisions**: The AI GM not only reacts to the player but can also introduce dynamic elements:
  - **Reinforcements**: On some missions, after a set number of turns or when the objective is nearly complete, the AI might call in enemy reinforcements. In XCOM 2, this is shown by a flare; here the AI can simply spawn a new pod at the edges. The system would announce “Enemy reinforcements inbound!” and one round later, spawn a pod (e.g., 2 Advent Troopers and 1 Advent MEC). This keeps the pressure on. The AI decides this based on mission type or if the players took too long (turn count).
  - **Targeting Priorities**: Enemies will make smart choices to challenge the player. For example, they focus fire on soldiers who are out of cover or wounded (to try to eliminate one). They use grenades on clumped soldiers. The AI’s decision algorithms incorporate these priorities. This can be done with simple evaluations (score potential actions by expected damage or outcome, pick the highest).
  - **Fallback and Regroup**: If aliens are getting wiped out, some might retreat or call for aid (particularly Officers). The AI could have an Officer use one action to radio reinforcements (functionally doing nothing visible but maybe guaranteeing an extra reinforcement pod arrives sooner). Or an enemy under half health might try to fall back to a better position instead of continuing to trade fire. These touches make the AI feel more organic, though they are optional for streamlined play.
  - **Mission Outcome**: The AI monitors win/loss conditions throughout. If an objective is completed (e.g., the player rescued the VIP and everyone is at the evac point), it will end the mission successfully. If a fail condition happens (squad wiped, or time expired for a critical mission), it will end with failure, possibly triggering a retreat or cutscene. These checks are simple if-statements in the main loop.

- **Objective Interaction**: The system should allow interactions like hacking a workstation or disarming a bomb. The AI can designate certain grid locations as **objective points**. When a soldier is adjacent and uses the correct action (e.g. the Specialist uses the Hack ability on a workstation), the AI rolls a hack attempt (Tech skill vs TN depending on objective difficulty). A success might immediately complete the mission (if that was the sole goal) or add a benefit (e.g., gained intel, or enemy robots shut down). A failure might spawn additional enemies or trigger an explosion (this can be pre-defined per mission type). This adds a layer of non-combat resolution that still uses our mechanics.

- **Python Implementation Notes**: The mission generation and AI behavior lend themselves to a rule-based or state-machine approach. For instance:
  ```python
  mission = generate_mission(objective="Rescue VIP")
  while mission.active:
      if player_turn:
          for soldier in squad:
              decide_and_execute_action(soldier)
              if mission.check_end_conditions(): break
          player_turn = False
      else:
          for pod in mission.alien_pods:
              for alien in pod:
                  decide_and_execute_action(alien)
                  ...
          player_turn = True
      mission.turn_count += 1
      handle_reinforcement_drop(mission.turn_count)
  ```
  The `decide_and_execute_action(alien)` function contains the behavior logic for each alien type described earlier. The AI uses the enemy’s stat block to pick an action (move, shoot, ability) and executes it. 
  The map can be stored as a grid of objects or IDs; pathfinding can be simplified with straight-line movement or a BFS for exact shortest paths if needed. Cover evaluation can be done by checking adjacent cells of an obstacle relative to shooter-target line.

- **Example**: Suppose the mission is Search & Destroy in a city block. The AI places 3 pods. The XCOM squad starts concealed at south end. As they advance, they see a Sectoid + 2 Advent pod. The Mission AI runs their patrol until the squad decides to ambush. Once shots are fired, the Mission AI activates that pod and possibly one nearby (if they heard the gunfire). The fight ensues with the enemy AI as described. Mid-mission, an Advent dropship arrives with reinforcements (triggered because the squad took 4 turns already and the objective isn’t finished). The AI spawns those at the north end with a 1-turn delay warning. Finally, once all initial enemies are down, if Search & Destroy, the mission ends successfully; if there was an objective item, the squad would grab it before evac. The AI GM handles all these transitions (activation, spawning, victory check) automatically.

With these mission rules, the system creates a dynamic battlefield. The AI Game Master manages everything from the strategic layout to moment-to-moment tactics, delivering a self-running XCOM-style experience. The design ensures each element (from dice rolls to enemy behavior) is structured and coded as discrete, testable components, making it efficient to run and modify. 

