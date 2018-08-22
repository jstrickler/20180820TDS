#!/usr/bin/env python

import csv

with open('DATA/presidents.csv') as pres_in:
    rdr = csv.reader(pres_in)
    for row in rdr:
        # print(row)
        term, first_name, last_name, birthplace, birth_state, party = row
        print(first_name, last_name, party)
