# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 16:24:36 2022

Dasturlash asoslari

#38-DARS. KUTUBXONALAR

Author: Sunnatillo Xayrullayev
"""

import datetime as dt

hozir = dt.datetime.now()
print(hozir)

# Sanani ajratib olish

print(hozir.date())

# Vaqtni ajratib olish

print(hozir.time())

# Soatni ajratib olish
print(hozir.hour)

# Minut
print(hozir.minute)

# Secund
print(hozir.second)


# BUgun 
bugun = dt.date.today()
print(f"Bugungi sana: {bugun}")

ertaga = dt.date(2022, 7, 20)

print(f"Ertangi sana: {ertaga}")

# Faqatgina vaqt bilan ishlash 
hozir = dt.datetime.now()
vaqtHozir = hozir.time()
print(f"Hozir soat: {vaqtHozir}")


# Istalgan vaqtni qo'lda kiritish

vaqtKeyin = dt.date(2022, 7, 25)
print(vaqtKeyin)

# Ayirish operatori yordamida sanalar va vaqtlar orasidagi farqni topish mumkin
bugun = dt.date.today()
qurbonhayit = dt.date(2022, 7, 12)
farq = bugun-qurbonhayit
print(f"Qurbon Hayitdan {farq.days} kun o'tdi") 

# Vaqt oralig'ini sekundlarda yoki soatlarda chiqarish

hozir = dt.datetime.now()
openbudget = dt.datetime(2022, 8, 2, 23, 00, 00)
farq = openbudget-hozir
sekundlar = farq.seconds
minutlar = int(sekundlar/60)
soatlar = int(minutlar/60)

print(f"Futbol boshlanishiga {sekundlar} sekund qoldi")
print(f"Futbol boshlanishiga {minutlar} minut qoldi")
print(f"Futbol boshlanishiga {soatlar} soat qoldi")
bugun = dt.date.today()
openbudget = dt.date(2022, 8, 3)
farq =openbudget-bugun
print(f"Ochiq byudjet registratsiyasiga {farq.days} kun qoldi")
