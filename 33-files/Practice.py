# -*- coding: utf-8 -*-
"""
Created on Fri May 27 15:19:32 2022

Dasturlash asoslari

#33-DARS. FILES PRACTISE

Author: Sunnatillo Xayrullayev
"""

with open ('knowlidge.txt') as file:
    knowlidge = file.read()
    
# print(knowlidge)

import pickle

with open ('pi_million_digits.txt') as file:
    pi = file.read()
    
pi = pi.rstrip()    # qator oxiridagi bo'shliqlarni olib tashlash
pi = pi.replace('\n', '')
pi = pi.replace(' ', '')    

pi = float(pi)
# print(type(pi))

with open("pinumbers.dat", "wb") as file:
    pickle.dump(pi, file)
    
# print(pi)

tyil = "20061991"
# print(tyil in pi)

# tyil = "3372448"

# if tyil in pi:
#     print(f"{tyil} pi ning tarkibida bor")
# else:
#     print(f"{tyil} pi ning tarkibida mavjud emas")

    
# with open("pinumbers", "rb") as file:
#     pi = pickle.load(file)


    

