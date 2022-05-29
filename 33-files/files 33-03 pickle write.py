# -*- coding: utf-8 -*-
"""
Created on Thu May 26 05:31:44 2022

Dasturlash asoslari

#33-DARS. FILES

Author: Sunnatillo Xayrullayev
"""

# O'ZGARUVCHILARNI FAYLDA SAQLASH

# PICKLE FAYLGA YOZISH

import pickle

talaba1 = {'ism':'hasan',   'familiya':'husanov',   'tyil':'2003',  'kurs':'2'}
talaba2 = {'ism':'Tolib',   'familiya':'usmonv',   'tyil':'2005',  'kurs':'3'}

with open ('talaba1', 'wb') as file:
    pickle.dump(talaba1, file)

with open ('talaba2.pkl', 'wb') as file:
    pickle.dump(talaba2, file)
