# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 06:34:12 2022

Dasturlash asoslari

30_lesson Inheritance

Author: Sunnatillo Xayrullayev
"""

# Vorislik va polimorfizm

class Shaxs:
    """Shaxslar haqida ma'lumot"""
    def __init__(self, ism, familiya, pasport, tyil):
        self.ism = ism
        self.familiya = familiya
        self.pasport = pasport
        self.tyil = tyil
        
    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}."
        info += f" Pasport: {self.pasport}, {self.tyil}-yilda tug'ilgan"
        return info
    
    def get_age(self, yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil-self.tyil
    
inson = Shaxs("Hasan", "Salomov", "AC123456", 1996)
print(f"{inson.get_info()}. {inson.get_age(2022)} yoshda.")
    
# VORIS KLASS YARATISH

# class Talaba(Shaxs):
#     """Talaba klassi"""
#     def __init__(self, ism, familiya, pasport, tyil):
#         """talabaning xususiyatlari"""
#         super().__init__(ism, familiya, pasport, tyil)
        
# talaba = Talaba("Valijon", "Aliyev","AA123654",2000)
# print(talaba.get_info())
# print(talaba.get_age(2022))

# VORIS KLASSGA XOS XUSUSIYATLAR VA METODLAR

# class Talaba(Shaxs):
#     """Talaba klassi"""
#     def __init__(self, ism, familiya, pasport, tyil, id):
#         """Talabaning xususiyatlari"""
#         super().__init__(ism, familiya, pasport, tyil)
#         self.idraqam = id
#         self.bosqich = 1
        
#     def get_id(self):
#         """Talabaning id raqami"""
#         return self.idraqam
    
#     def get_bosqich(self):
#         """Talabaning bosqichi"""
#         return self.bosqich
    
# talaba = Talaba("Abror", "To'laganov", "AB321456", 1995, "008356")

# print(f"{talaba.get_info()}. ID: {talaba.get_id()}")

# POLIMORFIZM-SUPER KLASS METODLARINI QAYTA YOZISH

class Talaba(Shaxs):
    """Talaba klassi"""
    def __init__(self, ism, familiya, pasport, tyil, id):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, pasport, tyil)
        self.idraqam = id
        self.bosqich = 1
        
    def get_id(self):
        """Talabaning id raqami"""
        return self.idraqam
    
    def get_bosqich(self):
        """Talabaning bosqichi"""
        return self.bosqich
    
    def get_info(self):
        """Talaba haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. Pasport: {self.pasport}."
        info += f" {self.tyil}-yilda tug'ilgan. ID: {self.idraqam}, {self.bosqich} - bosqich talabasi"
        return info
    
talaba = Talaba("Abror", "To'laganov", "AB321456", 1995, "008356")
print(talaba.get_info())


# OBYEKT ICHIDA OBYEKT

class Manzil:
    """Manzil saqlash uchun klass"""
    def __init__(self, uy, kocha, tuman, viloyat):
        """Manzil xususiyatlari"""
        self.uy = uy
        self.kocha = kocha
        self.tuman = tuman
        self.viloyat = viloyat
        
    def get_manzil(self):
        """Manzilni ko'rish"""
        manzil = f"{self.uy}-uy {self.kocha} ko'chasi "
        manzil += f"{self.tuman} tumani {self.viloyat} viloyati"
        return manzil
        
    
class Talaba(Shaxs):
    """Talaba klassi"""
    def __init__(self, ism, familiya, pasport, tyil, id, manzil):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, pasport, tyil)
        self.idraqam = id
        self.bosqich = 1
        self.manzil = manzil
        
    def get_id(self):
        """Talabaning id raqami"""
        return self.idraqam
    
    def get_bosqich(self):
        """Talabaning bosqichi"""
        return self.bosqich
    
    def get_info(self):
        """Talaba haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. Pasport: {self.pasport}."
        info += f" {self.tyil}-yilda tug'ilgan. ID: {self.idraqam}, {self.bosqich} - bosqich talabasi"
        return info    
    
manzil = Manzil(15, "Bog'bon", "Olmazor", "Toshkent")
talaba = Talaba("Abror", "To'laganov", "AB321456", 1995, "008356", manzil)

print(talaba.manzil.get_manzil())

print(talaba.manzil.viloyat)

# AMALIYOT

# talaba klassiga yana bir fanlar degan xususiyat qo'shing, bu xususiyat parametr sifatida uzatilmasin
# va obyekt yaratilganida bo'sh ro'yxatdan iborat bo'lsin

# class Talaba(Shaxs):
#     """Talaba klassi"""
#     def __init__(self, ism, familiya, pasport, tyil, id, manzil):
#         """Talabaning xususiyatlari"""
#         super().__init__(ism, familiya, pasport, tyil)
#         self.idraqam = id
#         self.bosqich = 1
#         self.manzil = manzil
#         self.fanlar = []
                
#     def get_id(self):
#         """Talabaning id raqami"""
#         return self.idraqam
    
#     def get_bosqich(self):
#         """Talabaning bosqichi"""
#         return self.bosqich
    
#     def get_info(self):
#         """Talaba haqida ma'lumot"""
#         info = f"{self.ism} {self.familiya}. Pasport: {self.pasport}."
#         info += f" {self.tyil}-yilda tug'ilgan. ID: {self.idraqam}, {self.bosqich} - bosqich talabasi"
#         return info    
    
    
class Fan:
    """Fan klassi"""
    def __init__(self, nomi, turi, muhimligi):
        self.nomi = nomi
        self.turi = turi
        self.muhimligi = muhimligi
                
    def get_fan(self):
        return f"{self.nomi} {self.turi} fan"
        
matem = Fan("Matematika", "tabiiy", "zarur")        
kimyo = Fan("Anorganik kimyo", "tabiiy", "o'rta")
iqtisod = Fan("Makro iqtisod", "ijtimoiy", "zarur")    
    
# Ro'yxatda yo'q fan uchun 
class Talaba(Shaxs):
    """Talaba klassi"""
    def __init__(self, ism, familiya, pasport, tyil, id, manzil):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, pasport, tyil)
        self.idraqam = id
        self.bosqich = 1
        self.manzil = manzil
        self.fanlar = []
                
    def get_id(self):
        """Talabaning id raqami"""
        return self.idraqam
    
    def get_bosqich(self):
        """Talabaning bosqichi"""
        return self.bosqich
    
    def get_info(self):
        """Talaba haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. Pasport: {self.pasport}."
        info += f" {self.tyil}-yilda tug'ilgan. ID: {self.idraqam}, {self.bosqich} - bosqich talabasi"
        return info    
    
    def fanga_yozil(self, fan):
        """Talabalarni fanga qo'shish"""
        self.fanlar.append(fan)
        
    def get_fanlar(self):
        """Talabaning fanlari haqida ma'lumot"""
        return [fan.get_fan() for fan in self.fanlar]
    
    def remove_fan(self, fan):
        """Talabaning fanlar ro'yxatdan biror fanni o'chirish"""
        if fan not in self.fanlar:
            print("Siz bu fanga yozilmagansiz") 
        else:
            return self.fanlar.remove(fan)
        
talaba1 = Talaba("Abror", "To'laganov", "AB321456", 1995, "008356", manzil)
talaba2 = Talaba("Hakim", "Islomov", "AC564231", 1897, "005343", manzil)

matem = Fan("Matematika", "tabiiy", "zarur")        
kimyo = Fan("Anorganik kimyo", "tabiiy", "o'rta")
iqtisod = Fan("Makro iqtisod", "ijtimoiy", "zarur")

talaba1.fanga_yozil(matem)
talaba2.fanga_yozil(kimyo)
talaba1.fanga_yozil(iqtisod)

talaba1.remove_fan(kimyo)

print(talaba1.fanlar)

print(talaba1.get_fanlar())
print(talaba2.get_fanlar())

# Yuqoridagi Shaxs klassidan boshqa turli voris klasslar yaratib ko'ring (masalan Professor,
# Foydalanuvchi, Sotuvchi, Mijoz va hokazo)

class Professor(Shaxs):
    """Professor klassi"""
    def __init__(self, ism, familiya, pasport, tyil, fan, institut):
        """professor xususiyatlari"""
        super().__init__(ism, familiya, pasport, tyil)
        self.fan = fan
        self.institut = institut
        
    def get_fan(self):
        return self.fan
    
    def get_institut(self):
        return self.institut      
    
    def get_info(self):
        info = f"{self.ism} {self.familiya} Pasporti: {self.pasport}. {self.tyil} da tug'ilgan. "
        info += f"{self.fan} bo'yicha {self.institut} professori"
        return info
        
professor1 = Professor("Umar", "Yigitaliyev", "AA000000", 2019, "IT", "MIT")
        
class Foydalanuvchi(Shaxs):
    """Foydalanuvchi klassi"""
    def __init__(self, ism, familiya, pasport, tyil, login, parol):
        """Foydalanuvchi xususiyatlari"""
        super().__init__(ism, familiya, pasport, tyil)
        self.login = login
        self.parol= parol
    
    def get_login(self):
        return self.login
    
    def get_parol(self):
        return self.parol
        
    def get_info(self):
        info = f"{self.ism} {self.familiya} Pasporti: {self.pasport}. {self.tyil} da tug'ilgan. "
        info += f"Foydalanuvchi logini: {self.login}, parol: {self.parol}"
        return info
    
user1 = Foydalanuvchi("Salim", "Halimov", "AC789654", 1998, "@Salimboy", 9999)
print(user1.get_info())

class Admin(Foydalanuvchi):
    """Admin klassi"""
    def __init__(self, ism, familiya, pasport, tyil, login, parol):
        """Admin xususiyatlari"""
    
        
    def ban_user(self):
        """Foydalanuvchini bloklash"""
        return f"Foydalanuvchi bloklandi"
    
user2 = Admin("Nematillo", "Isayev", "AC321654", 1992, "@nemat", 8975)
user1 = Admin("Salim", "Halimov", "AC789654", 1998, "@Salimboy", 9999)