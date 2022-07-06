# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 12:12:53 2022

Dasturlash asoslari

#35-DARS. DASTURNI TEKSHIRISH

Author: Sunnatillo Xayrullayev
"""

# FUNKSIYANI TEKSHIRISH

def get_fullname(ism, familiya, otasi = ''):
    if otasi:
        return f"{ism} {otasi} {familiya}".title()
    else:
        return f"{ism} {familiya}".title()

print(get_fullname('alijon', 'valiyev'))