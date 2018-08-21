#!/usr/bin/env python


list1 = list()  # new, empty list

cities = ['Middleton', 'Spring Green', 'Madison', 'Forest', 'Green Bay']

list2 = []  # also new, empty list

x = "wombats"

letters = list(x)  # loop over x and add each character to list

print(letters)

words = 'acme banana cauliflower date'.split()  # split string into words using space as sep
print(words)

pirate_words = ['yo', 'ho', 'ho']

p = list(pirate_words)

print(p)

# m.split()
# "foo".split()

#   somefunc(x)  builtin function
#   x.somefunc()  method (because it's called from an object)


cities = ['Middleton', 'Spring Green', 'Madison', 'Forest', 'Green Bay']

cities.append('Milwaukee')

print(cities)

cities.insert(0, 'Oconomowoc')
print(cities)
cities.insert(4, 'Stevens Point')
print(cities)

more_cities = ['Racine', 'Kenosha', 'Whitewater']

cities.extend(more_cities)

print(cities)

del cities[0]
print(cities)
del cities[8]
print(cities)

cities.remove('Racine')

print(cities)

city = 'Forest'
if city in cities:
    cities.remove(city)

print(cities)

position = cities.index('Green Bay')
print(position)

cities[position] = 'Dallas'

print(cities)


