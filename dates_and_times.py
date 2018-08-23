#!/usr/bin/env python

from datetime import date

today = date.today()

print(today, today.month, today.year, '\n')

tom_bd = date(1943, 8, 23)

print(tom_bd)

diff = today - tom_bd

print(diff)

age = round(diff.days / 365.25, 1)

print(age)

