#!/usr/bin/env python

import sys

print(sys.prefix)
print(sys.executable)
print()

print(sys.version)
print(sys.version_info)
print()

for path in sys.path:
    print(path)
print()

print(sys.platform)
print()


print("{:,d}\n".format(sys.maxsize))


sys.stdout.write("Hello hello\n")
sys.stderr.write("Help! Help!\n")



