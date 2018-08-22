#!/usr/bin/env python
from pprint import pprint

def get_letter_grade(score):
    if score > 94:
        grade = 'A'
    elif score > 88:
        grade = 'B'
    elif score > 82:
        grade = 'C'
    elif score > 74:
        grade = 'D'
    else:
        grade = 'F'

    return grade

# part 1
# create a dict
# open data file
# for line in data file
#    parse name and score
#    convert score to int
#    get letter grade
#    add data to dict where key is student, value is [score, grade]

# part 2
# for each student in sorted dictionary of students:
#    print student, score, grade

data = {}
with open('DATA/testscores.dat') as scores_in:
    for raw_line in scores_in:
        name, raw_score = raw_line.split(':')
        score = int(raw_score)
        grade = get_letter_grade(score)
        data[name] = score, grade

# pprint(data)
for name, scores in sorted(data.items()):
    print("{:20s} {:2d} {}".format(name, scores[0], scores[1]))

