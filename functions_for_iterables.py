#!/usr/bin/env python

colors = ['red', 'purple', 'ecru', 'brown', 'khaki', 'pink', 'green']

for color in colors:
    print(color)

for t in enumerate(colors):
    print(t)
print()

for i, color in enumerate(colors):
    print(i, color)
    if i == 4:
        print("Leeloo!")
print()


for i, color in enumerate(colors, 1000):
    print(i, color)
    if i == 4:
        print("Leeloo!")
print()
