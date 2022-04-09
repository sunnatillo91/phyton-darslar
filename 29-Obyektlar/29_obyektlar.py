# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 23:53:24 2022

Dasturlash asoslari

29-dars OBYEKTLAR BILAN ISHLASH

Author: Sunnatillo Xayrullayev
"""

# Xususiyatlarga standart qiymat berish

# class Talaba:
#     """Talaba nomli klass yaratamiz"""
#     def __init__(self,ism,familiya,tyil):
#         """Talabaning xususiyatlari"""
#         self.ism=ism
#         self.familiya=familiya
#         self.tyil=tyil
#         self.bosqich=1
        
#     def get_info(self):
#         return f"{self.ism} {self.familiya}, {self.bosqich}-bosqich talabasi"
    
# talaba1=Talaba("Alijon",'Valiyev', 1993)
# print(talaba1.get_info())

# # Standart qiymatni o'zgartirish

# talaba1.bosqich=2
# print(talaba1.bosqich)

# class Talaba:
#     """Talaba nomli klass yaratamiz"""
#     def __init__(self,ism,familiya,tyil):
#         """Talabaning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
#         self.bosqich = 1
    
#     def get_info(self):
#         """Talaba haqida ma'lumot"""
#         return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi "
    
#     def set_bosqich(self,bosqich):
#         """Talabaning kursini yangilovchi metod"""
#         self.bosqich = bosqich  
        
# talaba1.set_bosqich(3)
# print(talaba1.get_info())        

class Talaba:
    """Talaba nomli klass yaratamiz"""
    def __init__(self,ism,familiya,tyil):
        """Talabaning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.bosqich = 1
    
    def get_info(self):
        """Talaba haqida ma'lumot"""
        return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi "
    
    def set_bosqich(self,bosqich):
        """Talabaning kursini yangilovchi metod"""
        self.bosqich = bosqich
        
    def update_bosqich(self):
        """Talabanining bosqichini 1taga ko'paytirish"""
        self.bosqich += 1
        
talaba1 = Talaba("Alijon","Valiyev",2000)
print(talaba1.get_info())

talaba1.update_bosqich() # 1 bosqichga oshiramiz
print(talaba1.get_info())        

talaba1.update_bosqich() # 1 bosqichga oshiramiz
print(talaba1.get_info())

# OBYEKTLAR O'RTASIDA MUNOSABAT

class Fan():
    def __init__(self,nomi):
        self.nomi = nomi
        self.talabalar_soni = 0
        self.talabalar = []
    
    def add_student(self,talaba):
        """Fanga talabalar qo'shish"""
        self.talabalar.append(talaba)
        self.talabalar_soni += 1
   
    def get_students(self):
        """Fanga yozilgan talabalar haqida ma'lumot qaytaradi"""
        return [talaba.get_info() for talaba in self.talabalar]
                
matematika = Fan("Oliy Matematika")
talaba1 = Talaba("Alijon","Valiyev",2000)
talaba2 = Talaba("Hasan","Alimov",2001)
talaba3 = Talaba("Akrom","Boriyev",2001)       

matematika.add_student(talaba1)
matematika.add_student(talaba2)
matematika.add_student(talaba3)

print(matematika.talabalar_soni) 
    
mat_talabalar=matematika.get_students()
print(mat_talabalar)    


def see_methods(klass):
    return [method for method in dir(klass) if method.startswith('__') is False]

see_methods(Talaba)
print(see_methods(Fan))

print(talaba1.__dict__)
print(talaba1.__dict__.keys())

print(see_methods(talaba2))

# Amaliyot

# Avto degan yangi klass yarating. Unga avtomobillarga doir bo'lgan bir nechta xususiyatlar (model, rang, 
# korobka, narh va hokazo) qo'shing. Ayrim xususiyatlarga standart qiymat bering (masalan, kilometer=0)
# class Avto:
#     """Avto nomli klass yaratamiz"""
#     def __init__(self,model,rang,korobka,narx,yil):
#         """Avtoning xususiyatlar"""
#         self.model=model
#         self.rang=rang
#         self.korobka=korobka
#         self.narx=narx
#         self.yil=yil
#         self.kilometr=0
    
   
# Avto ga oid obyektning xususiyatlarini qaytaradigan metodlar yozing

# class Avto:
#     """Avto nomli klass yaratamiz"""
#     def __init__(self,model,rang,korobka,narx,yil):
#         """Avtoning xususiyatlar"""
#         self.model=model
#         self.rang=rang
#         self.korobka=korobka
#         self.narx=narx
#         self.yil=yil
#         self.kilometr=0
        
#     def get_model(self,model):
#         """Avtoning modeli"""
#         self.model=model
        
#     def get_rang(self,rang):
#         """Avtoning rangi"""
#         self.rang=rang
        
#     def get_korobka(self,korobka):
#         self.korobka=korobka
       
#     def get_narx(self,narx):
#         """Avto narxi"""
        
        
# get_info() metodi avto haqida to'liq ma'lumotni matn ko'rinishida qaytarsin

class Avto:
    """Avto nomli klass yaratamiz"""
    def __init__(self,model,rang,korobka,narx,yil):
        """Avtoning xususiyatlar"""
        self.model=model
        self.rang=rang
        self.korobka=korobka
        self.narx=narx
        self.yil=yil
        self.kilometr=500
        
    def get_model(self,model):
        """Avtoning modeli"""
        return self.model
        
    def get_rang(self,rang):
        """Avtoning rangi"""
        return self.rang
        
    def get_korobka(self,korobka):
        return self.korobka
       
    def get_narx(self,narx):
        """Avto narxi"""
        return self.narx
        
    def get_yil(self,yil):
        """Avto yili"""
        return self.yil
    def get_kilometr(self, kilometr):
        return self.kilometr
        
    def get_info(self):
        """Avto haqida to'liq ma'lumot"""
        return f"{self.model} {self.rang} {self.korobka} {self.narx} {self.yil} {self.kilometr}"
    
avto1=Avto('Lacetti', 'qora', 'avtomat', 13000, 2021)    
avto2=Avto('Cobalt', 'oq', 'mexanika', 11000, 2022)
        
print(avto1.get_info())
print(avto2.get_info())

# Avto ga oid obyektning xususiyatlarini yangilaydigan metodlar yozing.
class Avto:
    """Avto nomli klass yaratamiz"""
    def __init__(self,model,rang,korobka,narx,yil):
        """Avtoning xususiyatlar"""
        self.model=model
        self.rang=rang
        self.korobka=korobka
        self.narx=narx
        self.yil=yil
        self.kilometr=500
        
    def get_model(self,model):
        """Avtoning modeli"""
        return self.model
        
    def get_rang(self,rang):
        """Avtoning rangi"""
        return self.rang
        
    def get_korobka(self,korobka):
        return self.korobka
       
    def get_narx(self,narx):
        """Avto narxi"""
        return self.narx
        
    def get_yil(self,yil):
        """Avto yili"""
        return self.yil
    def get_kilometr(self, kilometr):
        return self.kilometr
        
    def get_info(self):
        """Avto haqida to'liq ma'lumot"""
        return f"{self.model} {self.rang} {self.korobka} {self.narx} {self.yil} {self.kilometr}"
    
avto1=Avto('Lacetti', 'qora', 'avtomat', 13000, 2021)    
avto2=Avto('Cobalt', 'oq', 'mexanika', 11000, 2022)

# update_km() metodi son qabul qilib olib, avtomobilning yurgan kilometrajini yangilab borsin


# Yangi, Avtosalon degan klass yarating va kerakli xususiyatlar bilan to'ldiring (salon nomi, manzili, 
# sotuvdagi avtomobillar va hokazo)


# Avtosalonga yangi avtomobillar qo'shish uchun metod yozing


# Avtosalondagi avtomobillar haqida ma'lumot qaytaruvchi metod yozing


# Yuqoridagi obyektlar va ularga tegishli metodlarni tekshirib ko'ring
# dir() funksyasi va __dict__ metodi yordamida o'zingiz yozgan va Pythondagi turli klass va obyektlarning
# xususiyatlari va metodlarini toping (dir(str), dir(int) va hokazo)

