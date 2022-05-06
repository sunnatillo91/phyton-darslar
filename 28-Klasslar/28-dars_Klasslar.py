# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 17:09:43 2022

Dasturlash asoslari

28-dars KLASSLAR

Author: Sunnatillo Xayrullayev
"""

# PYTHONDA KLASSLAR

x = 10
print(type(x))

matn = "salom"
print(type(matn))

def salom_ber():
    print("Assalomu alaykum")
print(type(salom_ber))    

# METODLAR

# Har bir obyekt uning ustida bajarish mumkin bo'lgan funksiyalar bilan keladi. Bu funksiyalar obyekt 
# ichida yashirin bo'ladi, va biz ularga nuqta va funksiya nomi orqali murojat qilishimiz mumkin. Bunday
# funksiyalar shu klass (yoki obyektga) tegishli metodlar deyiladi.

matn = "salom"
print(matn.upper())

# Bir klassga tegishli metodlar, boshqa klassdagi obyketlar uchun mavjud bo'lmasligi tabiiy.
#  Misol uchun matnlar uchun mavjud metodlarni, butun yoki o'nli sonlarga qo'llab bo'lmaydi.

son = 20
# print(son.lower())
# AttributeError: 'int' object has no attribute 'lower'

# KLASS YARATISH

class Talaba:
    """Talaba nomli klass yaratamiz"""
    def __init__(self,ism,familiya,tyil):
        """Talabaning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil

# KLASSDAN OBYEKT YARATISH
        
talaba1 = Talaba("Alijon","Valiyev",1991)

# Obyektning xususiyatlarini ko'rish
 
print(talaba1.ism)        
print(talaba1.familiya)

# Klassdan bir nechta obyektlar yaratish

talaba2 = Talaba("Olim","Karimov",1998)
talaba3 = Talaba("Bahrom","Nodirov",1997)
talaba4 = Talaba("Salim","Karimov",1998)

print(talaba2.ism)
print(talaba3.familiya)

# KLASSGA METODLAR QO'SHAMIZ

class Talaba:
    """Talaba nomli klass yaratamiz"""
    def __init__(self,ism,familiya,tyil):
        """Talabaning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        
    def tanishtir(self):
        print(f"Ismim {self.ism} {self.familiya}."
              f" {self.tyil} yilda tug'ilganman")
        
    def get_name(self):
        """Talabaning ismini qaytaradi"""
        return self.ism

    def get_lastname(self):
        """Talabaning familiyasini qaytaradi"""
        return self.familiya
    
    def get_fullname(self):
        """Talabaning ism familiyasini qaytaradi"""
        return f"{self.ism} {self.familiya}"
    
    def get_age(self, yil):
        """Talabaning yoshini qaytaradi"""
        return yil-self.tyil
        
# Obyektning metodlariga murojaat etamiz

talaba1 = Talaba("Alijon","Valiyev",1991)
talaba4 = Talaba("Salim","Karimov",1998)
talaba3 = Talaba("Bahrom","Nodirov",1997)
print(talaba3.get_fullname())
print(talaba4.get_lastname())


# Argument qabul qiluvchi metodlar

print(talaba1.get_age(2022))

# pass OPERATORI   (pass operatoridan bo'sh metodlar yaratishda foydalanish mumkin. Bu operator vazifa bajarmaydi

# class User:
#     def __init__(self,name,username,email):
#         self.name = name
#         self.uname=username
#         self.mail=email
        
#     def describe():
#         pass
    
#     def get_email():
#         pass
    
# AMALIYOT

# Veb sahifa uchun user class tuzing va uning xususiyatlari sifatida ma'lumotlarni kiriting

# class User:
#     def  __init__(self, ism, avatar, email, code):
#         self.ism = ism
#         self.avatar = avatar
#         self.mail = email
#         self.code = code

# Klassga bir nechta metodlar qo'shing

class User:
    def  __init__(self, ism, avatar, email, code):
        self.ism = ism
        self.avatar = avatar
        self.mail = email
        self.code = code
        
    def get_name(self):
        return self.ism
    
    def get_avatar(self):
        return self.avatar

    def get_info(self):
        return f"Foydalanuvchi {self.avatar}, ismi: {self.ism}, email: {self.mail}"
    
# Klassdan bir nechta obyektlar yarating, uning xususiyat va metodlariga murojaat qiling

user1 = User("Abbos Turdiyev", "abbos1994", "turdiyev@mail.ru", 545656)
print(user1.get_name()) 
print(user1.get_info())


    
    


