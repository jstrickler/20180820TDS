#!/usr/bin/env python
from collections import defaultdict

d1 = dict()  # empty dictionary
state_caps = {'WI': ['Madison', 'Washington'], 'NC': ['Raleigh', 'Tryon'],
              'NV': ['Carson City', 'Elm']}
d3 = {}  # empty dictionary

data = [('wombat', 6), ('anaconda', 2), ('wallaby', 5)]
d4 = dict(data)

print(state_caps.keys(), state_caps.values())
print(d4.keys(), d4.values())

print(state_caps.items())

for state, capital in state_caps.items():
    print(state, capital)

state_caps['CO'] = ['Denver', 'Mountain']

print(state_caps)

print(len(state_caps))

state = 'VA'
print(state_caps.get(state))
print(state_caps.get(state, 'NOT FOUND'))

def zero():
    return 0

d = defaultdict(zero)
d['a'] = 5
d['m'] = -4
d['p'] = 12

print(d['a'], d['x'], d['p'])


del state_caps['NV']
print(state_caps)

if 'WI' in state_caps:
    print(state_caps['WI'])


for state, (cap, street) in state_caps.items():
    print(state, cap)


countries = {
    'US': {
        'WI': 'Madison',
        'NC': 'Raleigh',
    },
    'CA': {
        'QB': 'Montreal',
        'ON': 'Toronto',
    }

}

for country, states in countries.items():
    print(country)
    for state, cap in states.items():
        print("\t", state, cap)

print(countries['US']['NC'])


