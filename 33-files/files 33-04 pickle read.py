# -*- coding: utf-8 -*-
"""
Created on Thu May 26 05:31:44 2022

Dasturlash asoslari

#33-DARS. FILES

Author: Sunnatillo Xayrullayev
"""

# O'ZGARUVCHILARNI FAYLDA SAQLASH

# PICKLE FAYLDAN O'QISH

import pickle

with open('talaba1', 'rb') as file:
    talaba1 = pickle.load(file)

with open('talaba2', 'rb') as file:
    talaba2 = pickle.load(file)

print(talaba1)
print(talaba2)