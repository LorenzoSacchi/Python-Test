#!/usr/local/bin/python3

import re
import os

path = os.listdir('/Users/lsa27/tatest')
regex = "fi(.*)?e"
for i in path:
    search = re.search(regex,i)
    if search:
        print(search.string)

    

