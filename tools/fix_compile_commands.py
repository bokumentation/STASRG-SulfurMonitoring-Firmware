# Author: Kondal Kolipaka <kondal.kolipaka@espressif.com>
#
# Copyright 2025 Espressif Systems (Shanghai) PTE LTD. All rights reserved.
# Use is subject to license terms.

"""
This script is used to remove all '-m*' and '-f*' flags from the compile_commands.json file.

Usage:
    python tools/fix_compile_commands.py <project_dir>
    python tools/fix_compile_commands.py example/ina219_test
"""

import os
import sys
import json
import re

def find_compile_commands_json(start_dir):
    for root, dirs, files in os.walk(start_dir):
        if 'compile_commands.json' in files:
            return os.path.join(root, 'compile_commands.json')
    return None

def remove_mf_flags(compile_commands):
    for entry in compile_commands:
        args = entry.get("arguments") or entry.get("command", "").split()
        filtered_args = [arg for arg in args if not re.match(r"^-([mf]).*", arg)]

        if "arguments" in entry:
            entry["arguments"] = filtered_args
        elif "command" in entry:
            entry["command"] = " ".join(filtered_args)
    return compile_commands

def main():
    if len(sys.argv) > 1:
        project_dir = sys.argv[1]
    else:
        project_dir = os.path.dirname(__file__)

    build_dir = os.path.join(project_dir, "build")
    cc_path = find_compile_commands_json(build_dir)

    if not cc_path:
        print("compile_commands.json not found.")
        return

    with open(cc_path, "r") as f:
        compile_commands = json.load(f)

    cleaned_commands = remove_mf_flags(compile_commands)

    with open(cc_path, "w") as f:
        json.dump(cleaned_commands, f, indent=2)

    print(f"Removed all '-m*' and '-f*' flags from: {cc_path}")

if __name__ == "__main__":
    main()
