# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 18:13:29 2022

Dasturlash asoslari

24-03-dars FUNKSIYALAR filter() FUNKSIYASI
"""

# filter() FUNKSIYASI

# import random as r
# sonlar = r.sample(range(100), 10)
# def juftmi(x):
#     """x juft bo'lsa True aks holda False qaytaramiz"""
#     return x%2==0

# juft_sonlar = list(filter(juftmi, sonlar))
# print(sonlar)
# print(juft_sonlar)

# # endi shu dasturni lambda yordamida yozamiz

# import random as r
# sonlar = r.sample(range(100), 10)
# juft_sonlar = list(filter(lambda son: son%2==0, sonlar))

# print(sonlar)
# print(juft_sonlar)

# mevalar = ['olma','anor','anjir',"o'rik",'qovun','banan']
# # mevB = list(filter(lambda meva:meva.startswith('b'), mevalar))
# # print(mevB)

# # mevalar2 = list(filter(lambda meva: len(meva)<=4, mevalar))
# # print(mevalar2)

# mevalar3 = list(filter(lambda meva: meva.startswith('a') and meva.endswith('r'), mevalar))
# print(mevalar3)

# AMALIYOT

# BERILGAN SONNI 10 GA KO'PAYTIRUVCHI LAMBDA FUNKSIYA YOZING

# son = lambda x: x*10
# print(son(9))

# # Ikki son qabul qilib yig'indini qaytaruvchi lambda f-ya
# yigindi = lambda x,y:x+y
# print(yigindi(5, 8))

# random moduli ichidagi sample f-ya yordamida 0 dan 1000 gacha sonlar oralig'idagi tasodifiy 10 ta sonlar ro'yxati

# import random as r
# sonlar = r.sample(list(range(0,1000)), 10)
# print(sonlar)

# # map() va lambda f-ya yordamida sonlarning kvadratini hisoblang:
# # kvadratlar = list(map(lambda x: x*x, sonlar))
# # print(kvadratlar)

# # filter() va lambda f-ya yordamida ro'yxatdan toq sonlarni ajratib olish
# toq_sonlar = list(filter(lambda son: son%2==1, sonlar))
# print(toq_sonlar)

# Berilgan son tub bo'lsa, True, aks holda False qaytaruvchi f-ya yozing 

def tubmi(x):
    if x%2==0 or x<2:
        return False
    if x==2 or x==3:
        return True
    for i in range(3,x,2):
        if x%i==0:
            return False
    return True    
print(tubmi(1251))

# filter() va yuqoridagi f-ya yordamida 1 dan 10000gacha oraliqdagi tub sonlar ro'yxatini tuzing

tub_sonlar = list(filter(tubmi, range(1,10000)))
print(tub_sonlar)