#!/usr/bin/env python

# guess # from 1 to 25

min_value = 0
max_value = 26

# until the user exits
#     calculate the guess
#     ask user if guess is correct
#     if y then
#         exit
#     if h then
#         set max to guess
#     else if l then
#         set min to guess
#     else
#         print error message

while True:
    guess = (min_value + max_value) // 2
    user_input = input("Is {} your number? ".format(guess))
    if user_input == 'y':
        print("I got it!")
        break
    if user_input == 'h':
        max_value = guess
    elif user_input == 'l':
        min_value = guess
    elif user_input == 'q':
        break  # user gave up
    else:
        print("Please enter h, l, y, or q")
