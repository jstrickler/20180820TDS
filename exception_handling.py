#!/usr/bin/env python


nums = [8, 9.7, 6.3, 0, 5.4, 2.37, '123']

x = 23.45

for n in nums:
    try:
        result = x / n
    except ZeroDivisionError as err:
        print(err)
    except TypeError as err:
        print(err)
    else:  # if no exceptions
        print("result is:", result)
    finally:
        print("WOMBAT!!")


try:
    with open('wombat_diary.txt') as wd_in:
        pass

except FileNotFoundError as err:
    print(err)


for n in nums:
    try:
        result = x / n
    except Exception:
        pass

