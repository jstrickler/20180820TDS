#!/usr/bin/env python

import os
from datetime import datetime

FOLDER = 'DATA'
FILE = 'mary.txt'

file_path = os.path.join(FOLDER, FILE)

print("file path:", file_path)

file_size = os.path.getsize(file_path)
print("file size:", file_size)
raw_timestamp = os.path.getmtime(file_path)
print("raw timestamp:", raw_timestamp)
timestamp = datetime.fromtimestamp(raw_timestamp)
print("timestamp:", timestamp)
print(type(timestamp))
print(timestamp.ctime(), timestamp.year, timestamp.weekday())

print(os.path.dirname(file_path))
print(os.path.basename(file_path))
print(os.path.abspath(file_path))

print(os.path.isdir(file_path))
print(os.path.isfile(file_path))
print(os.path.isdir(FOLDER))
print(os.path.isfile(FOLDER))
print(os.path.exists(file_path))

files = [p for p in os.listdir('DATA') if os.path.isdir(os.path.join('DATA', p))]
print(len(files))


