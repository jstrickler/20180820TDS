#!/usr/bin/env python
import csv

with open("DATA/baby-names.csv") as baby_in:
    rdr = csv.reader(baby_in)
    header = next(rdr)  # consume first element of generator (i.e., first line of file)
    print("HEADER:", header)
    for i, row in enumerate(rdr):
        year, name, percent, gender = row
        print(name, percent)
        if i == 25:
            break

with open("DATA/baby-names.csv") as baby_in:
    rdr = csv.reader(baby_in)
    john_pct = [(r[0], r[2]) for r in rdr if r[1] == 'John']
    for year, pct in john_pct:
        print(year, pct)

with open("DATA/baby-names.csv") as baby_in:
    rdr = csv.DictReader(baby_in)
    for i, row in enumerate(rdr):
        print(row['name'], row['percent'])
        if i == 25:
            break
