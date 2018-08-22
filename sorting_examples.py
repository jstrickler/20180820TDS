#!/usr/bin/env python

fruits = ["pomegranate", "cherry", "apricot", "date", "Apple",
"lemon", "Kiwi", "ORANGE", "lime", "Watermelon", "guava",
"Papaya", "FIG", "pear", "banana", "Tamarind", "Persimmon",
"elderberry", "peach", "BLUEberry", "lychee", "GRAPE" ]

f1 = sorted(fruits)
print("f1:", f1, '\n')

nums = [800,80,1000,32,255,400,5,5000]
n1 = sorted(nums)
print("n1:", n1, '\n')

people = [
    ('Melinda', 'Gates', 'Gates Foundation'),
    ('Steve', 'Jobs', 'Apple'),
    ('Larry', 'Wall', 'Perl'),
    ('Paul', 'Allen', 'Microsoft'),
    ('Larry', 'Ellison', 'Oracle'),
    ('Bill', 'Gates', 'Microsoft'),
    ('Mark', 'Zuckerberg', 'Facebook'),
    ('Sergey','Brin', 'Google'),
    ('Larry', 'Page', 'Google'),
    ('Linus', 'Torvalds', 'Linux'),
]

p1 = sorted(people)
for p in p1:
    print(p)
print()

def ignore_case(f):
    # print("in ignore_case(): f is" ,f)
    return f.lower()


f2 = sorted(fruits, key=ignore_case)
print("f2:", f2, '\n')



