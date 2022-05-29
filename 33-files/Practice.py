# -*- coding: utf-8 -*-
"""
Created on Fri May 27 15:19:32 2022

Dasturlash asoslari

#33-DARS. FILES PRACTISE

Author: Sunnatillo Xayrullayev
"""

with open ('knowlidge.txt') as file:
    knowlidge = file.read()
    
print(knowlidge)

with open ('pi_million_digits.txt') as file:
    pi = file.read()
    
# print(pi)

tyil = "20061991"

tyil = "3372448"

if tyil in pi:
    print(f"{tyil} pi ning tarkibida bor")
else:
    print(f"{tyil} pi ning tarkibida mavjud emas")
    
tyil = "19061993"

# pi = float(pi)
# print(type(pi))

import pickle

with open("pinumbers", "wb") as file:
    pickle.dump(float(pi), file)
    
with open("pinumbers", "rb") as file:
    pi = pickle.load(file)
    
print(type(pi))
