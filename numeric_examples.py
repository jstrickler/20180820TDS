#!/usr/bin/env python

i1 =  1010
i2 = 0x1010
i3 = 0b1010
i4 = 0o1010

f1 = 123.456
f2 = 123.
f3 = .456
f4 = 1.2343e22

x = 22
y = 5

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x // y)
print(x ** y)
print(x % y)

x += 3
x *= 4
x /= 10
x -= 1
print(x)


v = '123'

print(type(v))

m = int(v)
n = float(v)

print(type(m), type(n))
print(m, n)

i = "DeadBeef"
print(int(i, 16))


x = str(123.456)

print(x)
print(type(x))


#  print(o1, o2, ...)

print(i, x, m, n)

print("|", "spam", "|")

print("|", "spam", "|", sep='')

print(i, x, m, n, sep="#")
print(i, x, m, n, sep=", ")
print(i, x, m, n, sep=" wombat ")
print(i, x, m, n, sep="")

print("TDS", end=' ')
print("Telecom")

a = 33.97
b = 4.3902

result = a / b

print("result is", result)

print("result is {:.2f}".format(result))

first_name = 'Betty'
last_name = 'Rubble'
city = 'Bedrock'

print("{} {} is from {}".format(first_name, last_name, city))

print("first_name last_name")
print(first_name, last_name)
print(first_name + last_name)

print(f"{first_name} {last_name} is from {city}")





