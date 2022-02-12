"""
Created on Sat Feb 12 14:14:09 2022

Dasturlash asoslari

24-02-dars FUNKSIYALAR map() FUNKSIYASI
"""

# map() FUNKSIYASI

from math import sqrt
sonlar = list(range(11))  # 0 dan 10 gacha sonlar ro'yxati
# ildizlar = list(map(sqrt,sonlar))
# print(ildizlar)

# sonlar = list(range(11))
# def daraja2(x):
#     """Berilgan sonning kvadratini qaytaruvchi funksiya"""
#     return x*x
# print(list(map(daraja2,sonlar)))

# # Endi xuddi shu misolni lambda yordamida yozamiz
# kvadratlar = list(map(lambda x:x*x, sonlar))
# print(kvadratlar)

# map() funksiyasi bo'lmaganda biz bunday dasturlarni for yordamida yozishimiz kerak bo'lar edi:
    
kvadratlar = []
for son in sonlar:
    kvadratlar.append(son*son)
print(kvadratlar)

a = [4,5,6]
b = [7,8,9]
a_plus_b = list(map(lambda x,y: x+y, a,b))
print(a_plus_b)

ismlar = ['hasan','husan','olim','umid']
print(list(map(lambda matn: matn.upper(), ismlar)))

