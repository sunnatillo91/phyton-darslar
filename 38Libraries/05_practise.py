# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 18:43:01 2022

Dasturlash asoslari

#38-DARS. KUTUBXONALAR Practise

Author: Sunnatillo Xayrullayev
"""

# AMALIYOT

import datetime as dt

#1 10 ta sana

ertaga_5 = dt.date(2022, 8, 6)
print(ertaga_5)

ertaga_4 = dt.date(2022, 8, 5)
print(ertaga_4)

ertaga_3 = dt.date(2022, 8, 4)
print(ertaga_3)

ertaga_2 = dt.date(2022, 8, 3)
print(ertaga_2)

ertaga_1 = dt.date(2022, 8, 2)

ertaga = dt.date(2022, 8, 1)

print(ertaga)  

bugun = dt.date.today()
print(bugun)

kecha = dt.date(2022, 7, 30)
print(kecha)

kecha_1 = dt.date(2022, 7,29)
print(kecha_1)

kecha_2 = dt.date(2022, 7, 28)
print(kecha_2)

kecha_3 = dt.date(2022, 7, 27)
print(kecha_3)

#2 Ramazon va Qyrbon Hayitigacha qolgan vaqt

bugun = dt.date.today()
ramazon = dt.date(2023, 4, 23)
farq = ramazon - bugun
print(f"Ramazonga {farq.days} kun qoldi")

qurbon_hayit = dt.date(2023, 7, 1)
farq2 = qurbon_hayit-bugun
print(f"Qurbon hayitiga {farq2.days} kun qoldi")

# 3 Tug'ilgan kundan bugungacha o'tgan vaqt

def tkun(tyil, bugun):
    """Tug'ilgan kundan bugungacha o'tgan vaqtni qaytaruvchi funksiya"""
    farq = tyil-bugun
    print(f"Tug'ilgan kundan bugungacha o'tgan vaqt: {farq}")

tyil = dt.date(1991, 6, 20)
bugun = dt.date.today()
print(tkun(tyil, bugun))
