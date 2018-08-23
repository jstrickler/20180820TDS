#!/usr/bin/env python

import os

with os.popen('netstat -an') as netstat_in:
    for raw_line in netstat_in:
        if "ESTABLISHED" in raw_line:
            print(raw_line.rstrip())
