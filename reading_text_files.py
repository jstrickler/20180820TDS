#!/usr/bin/env python

#   file_obj = open('FILE NAME')

#  /Users/jstrick/Desktop/py3intro/DATA/mary.txt

with open('DATA/mary.txt') as mary_in:
    for raw_line in mary_in:
        line = raw_line.rstrip()  # remove \n etc
        print(line)  # line does NOT have the \n on the end
print()

with open('DATA/mary.txt') as mary_in:
    print(mary_in)
    for raw_line in mary_in:
        line = raw_line.rstrip()  # remove \n etc
        words = line.split()
        print(words)
print()


with open('DATA/mary.txt') as mary_in:
    contents = mary_in.read()  # read ALL characters into string
    print(contents)
    print(len(contents))
print()

with open('DATA/mary.txt') as mary_in:
    all_lines = mary_in.readlines()  # read ALL lines into list of strings
    print(all_lines)
print()
