"""
Created on Sat Feb 12 10:54:35 2022

Dasturlash asoslari

23-dars MODULLAR codes math 
"""

# random MODULI

# randint(a,b) funksiyasi a va b oralig'idagi tasodifiy butun sonni qaytaradi

import random as r
son = r.randint(0, 100)
print(son)

# choice(x) berilgan x argumentning ichidan tasodifiy elementni qaytaruvchi funksiya. bunda x bir necha o'zgaruvchidan iborat bo'lishi kerak

# ismlar = ['olim', 'anvar','hasan','husan']
# ism = r.choice(ismlar)  # tasodifiy ism tanlaymiz
# print(ism)

# x = list(range(0,51,5))  # ro'yxat yaratamiz
# print(x)
# print(r.choice(x))  # tasodifiy element tanlaymiz

# shuffle(x) - x ichidagi elementlarni tasodifiy tartibda qaytaruvchi funksiya
x = list(range(11)) # ro'yxat yaratamiz
print(x)
r.shuffle(x)
print(x) # ro'yxatni aralashtirib tashlaymiz

# sample(x,k) - ro'yxat ichidan tasodifiy k ta element ajratib olish
from random import sample
x=list(range(0,100))
y=sample(x, k=10)
print(y)