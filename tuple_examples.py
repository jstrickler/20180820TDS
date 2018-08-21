#!/usr/bin/env python

person = 'Brad', 'Pitt', 'movies'

first_name, last_name, product = person

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

for person in people:
    print(person[0], person[1])
print()

for person in people:
    first_name, last_name, product = person
    print(first_name, last_name)
print()

for first_name, last_name, product in people:
    print(first_name, last_name)
print()


data = [
    ['A', 123],
    ['M', 765, 34, 5],
    ['R', 18],
]

for d in data:
    print(d, d[0], d[1])
print()

for letter, *numbers in data:
    print(letter, numbers)
print()

print(len(people))
print(len(people[0]))
print(len(people[0][0]))

junk = ['m', 'r', 'a', 'w', 'n']
nums = [800,80,1000,32,255,400,5,5000]

print(min(junk), max(junk))
print(min(nums), max(nums))

total = sum(nums)
print(total)

print(sorted(junk))
print(sorted(nums))




