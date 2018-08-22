#!/usr/bin/env python
"""
Read student data and print a report
"""
from pprint import pprint

def main():
    """
    Program entry point

    :return: None
    """
    kdata = read_data()
    print_data(kdata)

def get_letter_grade(score):
    """
    Calculate letter grade using defined scale

    :param score: score as integer
    :return: letter grade as 1-character string
    """
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

def read_data():
    """
    Read data from file and parse, then put into dictionary where key is
    knight name

    :return: student data as dictionary of tuples where key is name, value is score, grade
    """
    data = {}
    with open('DATA/testscores.dat') as scores_in:
        for raw_line in scores_in:
            name, raw_score = raw_line.split(':')
            score = int(raw_score)
            grade = get_letter_grade(score)
            data[name] = score, grade
    return data

def print_data(data):
    """
    Neatly display data

    :param data: dictionary of student data
    :return: None
    """
    for name, scores in sorted(data.items()):
        print("{:20s} {:2d} {}".format(name, scores[0], scores[1]))

if __name__ == '__main__':
    main()
