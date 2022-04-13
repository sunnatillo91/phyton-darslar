# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 06:07:09 2022

Dasturlash asoslari

30-dars VORISLIK VA POLIMORFIZM

Author: Sunnatillo Xayrullayev
"""

class Shaxs:
    """Shaxslar haqida ma'lumot"""
    def __init__(self, ism, familiya, passport, tyil):
         """Shaxsning xususiyatlari"""
         self.ism = ism
         self.familiya = familiya
         self.passport = passport
         self.tyil = tyil
    def get_info(self):
         """Shaxs haqida ma'lumot"""
         info = f"{self.ism} {self.familiya}. "
         info+=f"Passport:{self.passport} {self.tyil}-yilda tug'ilgan"
         return info
     
    def get_age(self,yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil-self.tyil
    
inson = Shaxs("Hasan", "Olimov","AB451254",1996)
print(f"{inson.get_info()}. {inson.get_age(2022)} yoshda.")  

# VORIS KLASS YARATISH

# class Talaba(Shaxs):
#     """Talaba klassi"""
#     def __init__(self,ism, familiya, passport, tyil):
#         """Talabaning xususiyatlari"""
#         super().__init__(ism, familiya, passport, tyil)
        
# talaba=Talaba("Valijon", "Aliyev", "AC145216", 1993)
# print(talaba.get_info())

# VORIS KLASSSGA XOS XUSUSIYATLAR 

class Talaba(Shaxs):
    def __init__(self, ism, familiya, passport, tyil,id):
        """Talabaning xususiyatlari"""
        super().__init__(ism,familiya,passport,tyil)
        self.idraqam = id
        self.bosqich = 1
        
    def get_id(self):
        """Talabaning ID raqami"""
        return self.idraqam
    
    def get_bosqich(self):
        """Talaba bosqichi"""
        return self.bosqich
    
talaba = Talaba("Qobil", "Halimov", "AC123456", 1995, "00654321")        
        
print(f"{talaba.get_info()}. ID:{talaba.get_id()}")

print(f"{talaba.get_bosqich()}-bosqich talabasi")

# POLIMORFIZM - SUPER-KLASS METODLARINI QAYTA YOZISH

class Talaba(Shaxs):
    """Talaba klassi"""
    def __init__(self, ism, familiya, passport, tyil, id):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)
        self.bosqich=1
        return self.idraqam
        
        def get_info(self):
            """Talaba haqida ma'lumot"""
            info = f"{self.ism} {self.familiya}."
            
            info+=f"{self.get_bosqich()}-bosqich. ID: {self.idraqam}"
            return info
print(talaba.get_info())

# OBYEKT ICHIDA OBYEKT

class Manzil:
    """Manzil saqlash uchun klass"""
    def __init__(self, uy, kocha, tuman,viloyat ):
        """Manzil xususiyatlari"""
        self.uy = uy
        self.kocha = kocha
        self.tuman = tuman
        self.viloyat = viloyat
        
        