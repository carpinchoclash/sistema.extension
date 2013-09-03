#!/usr/bin/env python
import sys
import os

app = sys.argv[1]
os.system('ps ax | grep '+app+' | grep -v grep | head -c 5 | xargs kill -9')



