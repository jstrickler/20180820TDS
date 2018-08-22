#!/usr/bin/env python

john_countries = """Canada
Mexico
Barbados
China
UK
Austria
Spain
Bulgaria
Israel""".split('\n')

clare_countries = """British Virgin Islands
Denmark
UK
Spain
Kenya
Mexico
Barbados
Norway
Sweden
Canada""".split('\n')


john = set(john_countries)
clare = set(clare_countries)

print("both:", john & clare)  # intersection (common)
print("either:", john | clare) # uniton (all)
print("just one:", john ^ clare) # xor (non-common)
print("just John:", john - clare)
print("just Clare:", clare - john)

ted = {'Spain', 'Kenya'}

print(clare - john - ted)
alice = {'UK', 'Kenya', 'Israel', 'Spain'}

print(clare & john & ted & alice)

