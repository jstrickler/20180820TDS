#!/usr/bin/env python

guy1 = 'Bob'
guy2 = 'Tim'

activity = 'fishing'

print(guy1, "and", guy2, "are going", activity)

s = "{} and {} are going {}".format(guy1, guy2, activity)

print(s)

fmt = "{:5d}"

print(fmt.format(25))
print(fmt.format(101))
print(fmt.format(1234))
print(fmt.format(9))

num = 23
print(f"{num:5d}")
