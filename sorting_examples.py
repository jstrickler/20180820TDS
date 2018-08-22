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


f3 = sorted(fruits, key=len)
print("f3:", f3, '\n')

f4 = sorted(fruits, key=len)[:5]
print("f4:", f4, '\n')

def len_and_name(wombat):
    return len(wombat), wombat.lower()

f5 = sorted(fruits, key=len_and_name)
print("f5:", f5, '\n')


def wacky(f):
    return f[1], f[-1]

f6 = sorted(fruits, key=wacky)
print("f6:", f6, '\n')

def by_last_name(p):
    return p[1], p[0]


p2 = sorted(people, key=by_last_name)
print("p2:", p2, '\n')
for person in p2:
    print(person)
print()

n2 = sorted(nums, key=str)
print("n2:", n2, '\n')


n3 = sorted(nums, key=str, reverse=True)
print("n3:", n3, '\n')


names = ['John', 'Mitchell', 'Kevin', 'Joe']

def more_wackier(n):
    print(n)
    return n[2]

print(sorted(names, key=more_wackier))


junk = [('A', 19, 'wombat'), ('R', 4, 'wallaby'), ('C', 85, 'dingo'), ('A', 2, 'sloth')]


print(sorted(junk))

def by_animal(x):
    print("x is:", x)
    return x[2]

print(sorted(junk, key=by_animal))

def by_number(x):
    return x[1]

print(sorted(junk, key=by_number))
print()

airports = {
    'EWR': 'Newark',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SAC': 'Sacramento',
    'IAD': 'Dulles',
}

def by_value(x):
    return x[1]

for abbr, name in sorted(airports.items(), key=by_value):
    print(abbr, name)
print()

for abbr, name in sorted(airports.items(), key=lambda x: x[1]):
    print(abbr, name)



















