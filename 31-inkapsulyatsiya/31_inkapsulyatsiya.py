# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 06:26:55 2022

Dasturlash asoslari

31_lesson INKAPSULYATSIYA, KLASSNING XUSUSIYAT VA METODLARI

Author: Sunnatillo Xayrullayev
"""

# from uuid import uuid4
# class Avto:
#     num_avto = 0
#     PI = 3.14159
#     """Avtomobil klassi"""
#     def __init__(self, make, model, rang, yil, narx, km=0):
#         """Avtomobilning xususiyatlari"""
#         self.make = make
#         self.model = model
#         self.rang = rang
#         self.yil = yil
#         self.__km = km
#         self.__id = uuid4()
#         Avto.num_avto += 1
        
#     def get_km(self):
#         return self.__km
    
#     def get_id(self):
#         return self.__id
    
#     def add_km(self, km):
#         """Mashinaning kmga km qo'shish"""
#         if km>=0:
#             self.__km += km
#         else:
#             return "Mashina km kamaytirib bo'lmaydi" 
    
# avto1 = Avto("GM", "Malibu", "qora", 2020, 400000, 100000)
# avto1.add_km(1500)
# print(avto1.get_km())

# har bir yangi yaratilgan avtomobilga yangi, noyob va takrorlanmas ID generasiya
# qilish uchun uuid4() funksiyasidan foydalanayapmiz. Deylik biz mashinalar sotish 
# uchun onlayn bozor yaratsak, bozorimizga qo'shilgan har bir moshina endi o'zining 
# ID raqamiga ega bo'ladi va bu ID raqamni to'g'ridan-to'g'ri (nuqta orqali) ko'rib bo'lmaydi.

# inkapsulatsiya qilingan xususiyatlarni ko'rish uchun alohida metodlar yozish talab qilinadi

# print(avto1.get_km())

# # KLASSNG XUSUSIYATLARI VA METODLARI

# avto1 = Avto("GM", "Malibu", "Qora", 2020, 40000)
# avto2 = Avto("GM", "Lacetti", "Oq", 2020, 20000)
# avto3 = Avto("Toyota", 'Carolla', "Silver", 2021, 35000)

# print(Avto.num_avto)
# # 4

# Klassning xususiyatlarini inkapsulyatsiya qilish

from uuid import uuid4
class Avto:
    __num_avto = 0
    PI = 3.14159
    """Avtomobil klassi"""
    def __init__(self, make, model, rang, yil, narx, km=0):
        """Avtomobilning xususiyatlari"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.__km = km
        self.__id = uuid4()
        Avto.__num_avto += 1
    
# Klassgaoid metodlar

    @classmethod
    def get_num_avto(cls):
        return cls.__num_avto
    
avto1 = Avto("GM", "Malibu", "Qora", 2020, 40000)
avto2 = Avto("GM", "Lacetti", "Oq", 2020, 20000)
avto3 = Avto("Toyota", 'Carolla', "Silver", 2021, 35000)

print(Avto.get_num_avto())


# @classmethod bu maxsus dekorator. Dekoratorlar - o'z ichiga funksiya oluvchi funksiyalar

