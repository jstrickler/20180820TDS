#!/usr/bin/env python
import sys
import os  # os.path
from tds.misc import tdsutil

for x in dir(sys):
    print("{:20s} {}".format(x, type(getattr(sys, x)).__name__))
