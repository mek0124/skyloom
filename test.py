import os
import time

bash_scripts_dir = "/home/mekasu0124/Documents/dev/ai/tools/bash"
script_count = 0

print("Starting script iteration\n")

for root, dir, modules in os.walk(bash_scripts_dir):
    for module in modules:
        if module.endswith('sh') and "textual" in module:
            script_path = os.path.join(root, module)
            print(f"Script Found: {script_path}")
            break
        
        script_count += 1

print(f"\nFinished: {script_count} scripts found")