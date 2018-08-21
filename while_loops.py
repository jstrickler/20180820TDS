#!/usr/bin/env python

while True:
    raw_height = input("How high is the water? ")
    if raw_height == 'q':
        print("goodbye")
        break  # exit the loop
    if raw_height == '':
        continue  # go back to top
    if raw_height.isdigit():
        height = int(raw_height)
        print("{} feet high and risin'".format(height))
    else:
        print("Please enter a number")

