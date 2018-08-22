#!/usr/bin/env python

import csv

name_counts = {}

with open("DATA/baby-names.csv") as baby_in:
    rdr = csv.reader(baby_in)
    for year, name, percent, gender in rdr:
        if name in name_counts:
            name_counts[name] = name_counts[name] + 1
        else:
            name_counts[name] = 1

        # name_counts[name] = name_counts.get(name, 0) + 1

print(len(name_counts))

print(name_counts['John'])
print(name_counts['Kyle'])
print(name_counts['Brittany'])

