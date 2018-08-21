#!/usr/bin/env python

r = range(10)
# range(stop)  range(start, stop)  range(start, stop, incr)

for i in r:
    print(i)
print()

for i in range(1, 11):
    print(i)
print()

for i in range(10, 101, 10):
    print(i)
print()

for i in range(25):
    print("Wombat!")
print()


animals = ['wombat', 'honey badger', 'wildebeest']
numbers = [18, 4, 99, 26, 17, 42, 52]

combo = zip(animals, numbers)

for a, n in combo:
    print(a, n)

print(list(zip(animals, numbers)))
print()

r = range(10)
e = enumerate(animals)
combo = zip(animals, numbers)

print(r)
print(e)
print(combo)

