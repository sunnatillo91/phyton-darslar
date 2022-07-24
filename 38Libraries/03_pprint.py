# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 15:45:20 2022

Dasturlash asoslari

#38-DARS. KUTUBXONALAR  pprint

Author: Sunnatillo Xayrullayev
"""

from pprint import pprint
import json

filename = 'bemor.json'

with open(filename) as f:
    bemor = json.load(f)
    
print(bemor)
print(5)
pprint(bemor)