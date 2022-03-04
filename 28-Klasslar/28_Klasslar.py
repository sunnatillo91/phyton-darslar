# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 20:44:48 2022

Dasturlash asoslari

28-dars KLASSLAR

Author: Sunnatillo Xayrullayev

"""

x=10
print(type(x))

# KLASS YARATISH

class Talaba:
    """Talaba nomli klass yaratamiz"""
    def __init__(self,ism,familiya,tyil):
        """Talabaning xususiyatlari"""
        self.ism=ism
        self.familiya=familiya
        self.tyil=tyil
       
# Klassdan obyekt yaratish
        
talaba1=Talaba("Alijon",'Valiyev', 1993)
               
# Obyekttningg xususiyatlarini ko'rish

print(talaba1.ism)        
print(talaba1.tyil) 

# Klassdan bir nechta obyektlar yaratish

talaba2=Talaba("Olim",'Aliyev',1999)
talaba3=Talaba("Valijon",'Soliyev',2000)
talaba4=Talaba("Akrom",'Choriqulov',1991)
print(talaba3.ism)

# Klassga metodlar qo'shamiz

class Talaba:
    """Talaba nomli klass yaratamiz"""
    def __init__(self,ism,familiya,tyil):
        """Talabaning xususiyatlari"""
        self.ism=ism
        self.familiya=familiya
        self.tyil=tyil
        
    def tanishtir(self):
        print(f"Ismim {self.ism} familiyam {self.familiya}."
            f"{self.tyil} yilda tug'ilganman")
        
talaba4=Talaba("Akrom",'Choriqulov',1991)
talaba4.tanishtir()
        
       