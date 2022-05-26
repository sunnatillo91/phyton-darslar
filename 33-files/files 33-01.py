# -*- coding: utf-8 -*-
"""
Created on Thu May 26 05:31:44 2022

Dasturlash asoslari

#33-DARS. FILES

Author: Sunnatillo Xayrullayev
"""

with open ('pi.txt') as file:
    pi = file.read()
    
# print(pi)

pi = pi.rstrip()    #qator oxiridagi bo'shliqlarni olib tashlaymiz
pi = pi.replace('\n', '')       # qator tashlash belgisini almashtiramiz
pi = float(pi)     # matnni float(o'nlik) songa o'tkazamiz)
print(pi)

# PAPKA ICHIDAGI FAYLLARNI OCHISH

with open ('files/data/pi.txt') as file:
    pi = file.read()
    
print(pi)

faylnomi = 'files/data/math/pi.txt'
with open (faylnomi) as file:
    pi = file.read()
    
print(pi)

# FAYLNI QATORMA-QATOR O'QISH

filename = 'files\\data\\talabalar.txt'
with open (filename) as file:
    for line in file:
        print(line)
        
with open (filename) as file:
    talabalar = file.readlines()
print(talabalar)

talabalar = [talaba.rstrip() for talaba in talabalar]
print(talabalar)

# FAYLGA MA'LUMOT YOZISH

