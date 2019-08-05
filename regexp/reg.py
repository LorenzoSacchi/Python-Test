#! /usr/local/bin/python3

import re
import os

"""
regexp test
"""

PATH = os.listdir('/Users/lsa27/tatest')
REGEX = "fi(.*)?e"
for i in PATH:
    search = re.search(REGEX, i)
    if search:
        print(search.string)
