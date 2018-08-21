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

ww = cities.pop()
print(ww)

print(cities)

x = cities.pop(3)
print(x)
print(cities)


print(cities[0], cities[4])

print(cities[-1])

print(cities)

x = cities.pop()
print(x)
print(cities)



cities = ['Middleton', 'Spring Green', 'Madison', 'Forest', 'Green Bay']
cities.append('Milwaukee')

print(cities)
print('\n')

cities.insert(0, 'Oconomowoc')
cities.insert(4, 'Stevens Point')

more_cities = ['Racine', 'Kenosha', 'Whitewater']

cities.extend(more_cities)

print(cities)

print(cities[0:3])  # first 3 cities
print(cities[4:7])  # 3 cities starting at cities[4]
print(cities[8:len(cities)])

print(cities[:3])
print(cities[8:])
print(cities[:])

city = "Oconomowoc"

print(city[:4])   #  [0:4]
print(city[3:6])
print(city[-5:])  #   [-5:len(city)]

print(cities)
print()

for city in cities:
    print(city, city.upper())
print()


colors = ['red', 'purple', 'ecru', 'brown', 'khaki', 'pink', 'green']

for wombat in colors:
    print(wombat)
print()

info = ['Mary', 'Smith', 'Racine']

first_name, last_name, city = info

print(first_name, last_name)

a, *b = info
print(a, b)

*a, b = info
print(a, b)


things = ['a', 'b', 'c', 'd', 'e', 'f']

*x, y, z = things
print(x, y, z)

x, *y, z = things
print(x, y, z)

x, y, *z = things
print(x, y, z)
print(x)
print(y)
print(z)








