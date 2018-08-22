#!/usr/bin/env python

def get_message():
    return "Hello, TDS world!"

def print_message():
    message = get_message()
    print(message)


print_message()


def get_file_contents(file_name):
    with open(file_name) as file_in:
        contents = file_in.read()
    return contents


mary = get_file_contents('DATA/mary.txt')

print(mary)


def spam(x, *y):
    print("x:", x)
    print("y:", y)


spam('a')
spam('a', 'b', 'c')
spam('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')

carnivore = 'wolverine'

animal = 'wallaby'

def ham():
    animal = 'wombat'   # LOCAL variable
    print(carnivore)

ham()

print(animal)


def toast(*args, **kwargs):
    pass






