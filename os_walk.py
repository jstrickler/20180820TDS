#!/usr/bin/env python
import os

FOLDER = os.path.abspath('.')

for curr_dir, folders, files in os.walk(FOLDER):
    if 'git' in curr_dir:
        continue
    print(curr_dir)
    for file_name in files:
        if file_name.endswith('.py'):
            file_path = os.path.join(curr_dir, file_name)
            file_size = os.path.getsize(file_path)
            print("    {:6d} {}".format(file_size, file_name))
