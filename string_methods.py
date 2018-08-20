#!/usr/bin/env python


celeb = "Brad Pitt"

print(celeb)

c2 = celeb.upper()
print(c2)
print(celeb.upper())

print(celeb)
print(c2)
print(len(celeb))

print(celeb.replace('Brad', 'Billy'))

c3 = celeb.replace('Brad', 'Beauregard')

print(c3)


print(celeb.count('t'))

print(celeb.count('Pit'))

print(celeb.startswith('B'))
print(celeb.startswith('t'))

print(celeb.endswith('B'))
print(celeb.endswith('t'))

print(celeb.lower().startswith('b'))

data = 'Mary Doe Middleton WI'

fields = data.split()
print(fields)
print()

s = "        All my exes live in Texas          "

print('|', s.lstrip(), '|')
print('|', s.rstrip(), '|')
print('|', s.strip(), '|')
print()

s = "xyxxyyxxxyyyAll my exes live in Texasxyxxxyyyxxyyxyxyxyxyx"

print('|{}|'.format(s.lstrip('xy')))
print('|', s.rstrip('xy'), '|')
print('|', s.strip('xy'), '|')
print()





