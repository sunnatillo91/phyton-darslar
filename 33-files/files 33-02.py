# -*- coding: utf-8 -*-
"""
Created on Thu May 26 05:31:44 2022

Dasturlash asoslari

#33-DARS. FILES

Author: Sunnatillo Xayrullayev
"""

# FAYLGA MA'LUMOT YOZISH

# YANGI FAYLGA YOZISH

faylnomi = 'new_file.txt'       # ochilayotgan fayl nomi
ism = 'Olimjon Hasanov'
tyil = 2004
with open (faylnomi, 'w') as fayl:
    fayl.write(ism+'\n')   #faylga yozilayotgan matn
    fayl.write(str(tyil)+'\n')

faylnomi = "new_file.txt"
with open (faylnomi, 'a') as fayl:
    fayl.write('Alijon Valiyev\n')
    fayl.write('2000')