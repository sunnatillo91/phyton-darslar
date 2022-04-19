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

# class Talaba(Shaxs):
#     def __init__(self, ism, familiya, passport, tyil,id):
#         """Talabaning xususiyatlari"""
#         super().__init__(ism,familiya,passport,tyil)
#         self.idraqam = id
#         self.bosqich = 1
        
#     def get_id(self):
#         """Talabaning ID raqami"""
#         return self.idraqam
    
#     def get_bosqich(self):
#         """Talaba bosqichi"""
#         return self.bosqich
    
# talaba = Talaba("Qobil", "Halimov", "AC123456", 1995, "00654321")        
        
# print(f"{talaba.get_info()}. ID:{talaba.get_id()}")

# print(f"{talaba.get_bosqich()}-bosqich talabasi")

# # POLIMORFIZM - SUPER-KLASS METODLARINI QAYTA YOZISH

# class Talaba(Shaxs):
#     """Talaba klassi"""
#     def __init__(self, ism, familiya, passport, tyil, id):
#         """Talabaning xususiyatlari"""
#         super().__init__(ism, familiya, passport, tyil)
#         self.bosqich=1
#         return self.idraqam
        
#         def get_info(self):
#             """Talaba haqida ma'lumot"""
#             info = f"{self.ism} {self.familiya}."
            
#             info+=f"{self.get_bosqich()}-bosqich. ID: {self.idraqam}"
#             return info
# print(talaba.get_info())

# # OBYEKT ICHIDA OBYEKT

class Manzil:
    """Manzil saqlash uchun klass"""
    def __init__(self, uy, kocha, tuman,viloyat ):
        """Manzil xususiyatlari"""
        self.uy = uy
        self.kocha = kocha
        self.tuman = tuman
        self.viloyat = viloyat

    def get_manzil(self):
        """Manzilni ko'rish"""
        manzil = f"{self.viloyat} viloyati, {self.tuman} tumani, "
        manzil += f"{self.kocha} ko'chasi, {self.uy} - uy"
        return manzil 
        
class Talaba(Shaxs):
    def __init__(self, ism, familiya, passport, tyil, id, manzil):
        """Talabaning xususiyatlari"""
        super().__init__(ism,familiya,passport,tyil)
        self.idraqam = id
        self.bosqich = 1
        self.manzil = manzil
        
    def get_id(self):
        """Talabaning ID raqami"""
        return self.idraqam
    
    def get_bosqich(self):
        """Talaba bosqichi"""
        return self.bosqich    
    
    def get_info(self):
        """Talaba haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}."
        info += f"{self.get_bosqich()} - bosqich. ID raqami: {self.idraqam}"
        return info
    
manzil = Manzil(12, "Olmazor", "Bog'bon", "Samarqand")
talaba = Talaba("Alijon", "Valiyev", "AC145623", 1992, "UD005125", manzil)
print(talaba.manzil.tuman)
print(talaba.manzil.get_manzil()) 

 # AMALIYOT

# Talaba klassiga yana bir, fanlar degan xususiyat qo'shing. Bu xususiyat parametr sifatida 
# uzatilmasin va obyekt yaratilganida bo'sh ro'yxatdan iborat bo'lsin (self.fanlar=[])
class Talaba(Shaxs):
    def __init__(self, ism, familiya, passport, tyil, id, manzil):
        """Talabaning xususiyatlari"""
        super().__init__(ism,familiya,passport,tyil)
        self.idraqam = id
        self.bosqich = 1
        self.manzil = manzil
        self.fanlar = []
        
    def get_id(self):
        """Talabaning ID raqami"""
        return self.idraqam
    
    def get_bosqich(self):
        """Talaba bosqichi"""
        return self.bosqich    
    
    def get_info(self):
        """Talaba haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}."
        info += f"{self.get_bosqich()} - bosqich. ID raqami: {self.idraqam}"
        return info

# Fan degan yangi klass yarating va bu klassdan turli fanlar uchun alohida obyektlar yarating.
class Fan:
    """Fan klassi"""
    def __init__(self, nomi):
        self.nomi = nomi
        self.talaba_soni = 0
        self.talabalar = []
        
kimyo = Fan("Anorganikkimyo")
tarix = Fan("Jahon tarixi")
matematika = Fan("Oliy matematika")
        
talaba1 = Talaba("Dilshod","Komilov","AB456292",1995,"005145",manzil)
talaba2 = Talaba("G'olib","Salomov","AC123456",1997,"0094568", manzil)
talaba3 = Talaba("Islamov", "Tolib", "AB243565",2001,"080569", manzil)

# Talaba klassiga fanga_yozil() degan yangi metod yozing. Bu metod parametr sifatida Fan klassiga
# tegishli obyektlarni qabul qilib olsin va talabani fanlar ro'yxatiga qo'shib qo'ysin.
class Talaba(Shaxs):
    def __init__(self, ism, familiya, passport, tyil, id, manzil):
        """Talabaning xususiyatlari"""
        super().__init__(ism,familiya,passport,tyil)
        self.idraqam = id
        self.bosqich = 1
        self.manzil = manzil
        self.fanlar = []
        
    def get_id(self):
        """Talabaning ID raqami"""
        return self.idraqam
    
    def get_bosqich(self):
        """Talaba bosqichi"""
        return self.bosqich    
    
    def fanga_yozil(self,name):
        """Fan klassiga oid obyektlarni qabul qilib talabani fanlar ro'yxatiga qo'shib qo'yadi"""
        self.talabalar.append(talaba)
        self.talaba_soni += 1
        
    def get_info(self):
        """Talaba haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}."
        info += f"{self.get_bosqich()} - bosqich. ID raqami: {self.idraqam}"
        return info

talaba1 = Talaba("Dilshod","Komilov","AB456292",1995,"005145",manzil)
talaba2 = Talaba("G'olib","Salomov","AC123456",1997,"0094568", manzil)
talaba3 = Talaba("Islamov", "Tolib", "AB243565",2001,"080569", manzil)

talaba1.fanga_yozil(kimyo)
# Talabaning fanlari ro'yxatidan biror fanni o'chirib tashlash uchun remove_fan() metodini yozing. 
# Agar bu metodga ro'yxatda yo'q fan uzatilsa "Siz bu fanga yozilmagansiz" xabarini qaytarsin.


# Yuqoridagi Shaxs klassidan boshqa turli voris klasslar yaratib ko'ring (masalan Professor,
# Foydalanuvchi, Sotuvchi, Mijoz va hokazo)
    
    
# Har bir klassga o'ziga hoz xususiyatlar va metodlar yuklang.


# Barcha yangi klasslar uchun get_info() metodini qayta yozib chiqing.


# Voris klasslardan yana boshqa voris klass yaratib ko'ring. Misol uchun Foydalanuvchi 
# klassidan Admin klassini yarating. 


# Admin klassiga foydalanuvchida yo'q yangi metodlar yozing, masalan, ban_user() metodi 
# konsolga "Foydalanuvchi bloklandi" degan matn chiqarsin.
   