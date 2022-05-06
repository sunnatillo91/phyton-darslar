# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 20:18:45 2022

Dasturlash asoslari

29-dars OBYEKTLAR BILAN ISHLASH

Author: Sunnatillo Xayrullayev
"""

# Xususiyatlarga standart qiymat berish

# class Talaba:
#     def __init__(self,ism,familiya,tyil):
#         """Talabaning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
#         self.bosqich = 1
        
#     def get_info(self):
#         return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi."
    
#     def set_bosqich(self, bosqich):
#         """Talabaning kursini yangilovchi metod"""
#         self.bosqich = bosqich
        
#     def update_bosqich(self):
#         """Talabaning bosqichini 1 taga ko'paytiradi"""
#         self.bosqich += 1
    
# talaba1 = Talaba("Salim", "Olimov",1997)
# print(talaba1.get_info())

# Standart qiymatni o'zgartirish
# 1-usul
# talaba1.bosqich = 2
# print(talaba1.bosqich)

# # 2-usul
# talaba1.set_bosqich(4)
# print(talaba1.get_info())

# # 3-usul
# talaba1 = Talaba("Salim", "Olimov",1997)
# print(talaba1.get_info())
# talaba1.update_bosqich()   # 1 bosqicha oshiramiz
# print(talaba1.get_info())
# talaba1.update_bosqich()
# print(talaba1.get_info())

# OBYEKTLAR O'RTASIDA MUNOSABAT

# class Fan():
#     def __init__(self, nomi):
#         self.nomi = nomi
#         self.talabalar_soni = 0
#         self.talabalar = []
        
#     def add_student(self, talaba):
#         """Fanga talabalar qo'shish"""
#         self.talabalar.append(talaba)
#         self.talabalar_soni +=1
        
#     def get_students(self):
#         return [talaba.get_info() for talaba in self.talabalar]
        
        
# matematika = Fan("Oliy matematika")
# talaba1 = Talaba("Jasur", "Ro'ziyev", 1994)
# talaba2 = Talaba("Olim", "Tog'ayev", 1984)
# talaba3 = Talaba("Salim", "Jo'rayev", 1998)

# # Talabalarni yangi fanga qo'shamiz

# matematika.add_student(talaba1)
# matematika.add_student(talaba2)
# matematika.add_student(talaba3)

# print(matematika.talabalar_soni)
# print(matematika.talabalar)  
# mat_talabalar = matematika.get_students()
# print(mat_talabalar)

# NUQTA YOKI METOD

class Talaba:
    """Talaba nomli klass yaratamiz"""
    def __init__(self,ism,familiya,tyil):
        """Talabaning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.bosqich = 1
        
    def set_bosqich(self, bosqich):
        """Talabaning kursini yangilovchi metod"""
        self.bosqich = bosqich
        
    def update_bosqich(self):
        self.bosqich += 1
        
    def get_info(self):
        """Talaba haqida ma'lumot"""
        return f"{self.ism} {self.familiya}. {self.bosqich} - bosqich talabasi"
        
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
        """Talbaning yoshini qaytaradi"""
        return yil-self.tyil
    
talaba1 = Talaba("Jasur", "Ro'ziyev", 1994)
talaba2 = Talaba("Olim", "Tog'ayev", 1984)
talaba3 = Talaba("Salim", "Jo'rayev", 1998)
print(talaba2.get_age(2022))
    
class Fan():
    "Fan nomlli klass"
    def __init__(self,nomi):
        self.nomi = nomi
        self.talabalar_soni = 0
        self.talabalar = []
        
    def add_student(self,talaba):
        """Fanga talabalar qo'shish"""
        self.talabalar.append(talaba)
        self.talabalar_soni += 1

    def get_name(self):
        """Fan nomi"""
        return self.nomi
    
    def get_students(self):
        """Fanga yozilgan talabalar haqida ma'lumot"""
        return [talaba.get_fullname() for talaba in self.talabalar]
    
    def get_students_num(self):
        """Fanga yozilgan talabalar soni"""
        return self.talabalar_soni
    
matematika = Fan("Oliy matematika")
talaba1 = Talaba("Jasur", "Ro'ziyev", 1994)
talaba2 = Talaba("Olim", "Tog'ayev", 1984)
talaba3 = Talaba("Salim", "Jo'rayev", 1998)

matematika.add_student(talaba1)
matematika.add_student(talaba2)
matematika.add_student(talaba3)

# OBYEKTNING XUSUSIYATLARI VA METODLARINI KO'RISH

# dir() FUNKSIYASI

# print(dir(Talaba))

def see_methods(klass):
    return [method for method in dir(klass) if \
            method.startswith('__') is False]
        
print(see_methods(Talaba))
print(see_methods(talaba2))

# __dict__ METODI

# bu metod obyektlarning xususiyatlarini lug'at ko'rinishida qaytaradi
print(talaba1.__dict__)
print(talaba1.__dict__.keys())

# AMALIYOT

# Avto klassini va xususiyatlarini yaratish
# Avto ga oid obyektning xususiyatlarini qaytaruvchi metodlar yozing    
# get_info metodi avto haqida to'liq ma'lumotni matn ko'rinishida qaytarsin    
# Avtoga oid obyektning xususiyatlarini yangilaydigan metodlar yozing            
# update_km() metodi son qaabul qabul qilib avtomobil yurgan kilometrajni yangilasin        

class Avto:
    """Avto nomli klass"""
    def __init__(self, model,rang,korobka,narx,yil):
        self.model = model
        self.rang = rang
        self.korobka = korobka
        self.narx = narx
        self.yil = yil
        self.kilometr = 0


    def get_model(self):
        """avtoning modeli"""
        return self.model

    def get_rang(self):
        """avtoning rangi"""
        return self.rang
    
    def get_korobka(self):
        """avtonig korobkasi"""
        return self.korobka
    
    def get_narx(self):
        """avto narxi"""
        return self.narx
    
    def get_yil(self):
        """avto yili"""
        return self.yil
    
    def get_distance(self):
        """avto yurgan masofasi"""
        return self.kilometr
    def get_info(self):
        """avto haqida to'liq ma'lumot"""
        return f"Avto modeli: {self.model}, rangi {self.rang} {self.korobka}. Narxi: {self.narx} \
{self.yil} yil {self.kilometr} km yurgan" 
    def set_rang(self, yangi_rang):
        """avto rangini yangilaydi"""
        self.rang = yangi_rang
   
    def set_yil(self, yangi_yil):
        """avto yilini yangilaydi"""
        self.yil = yangi_yil        
    
    def update_km(self, new_km):
        """Avto kilometrajini yangilaydi"""
        self.kilometr = new_km
        
class Avtosalon:
    """Yangi avtosalon"""
    def __init__(self, salon_nomi, manzili, sotuvdagi_avtolar):
        self.salon_nomi = salon_nomi
        self.manzili = manzili
        self.sotuvdagi_avtolar = sotuvdagi_avtolar 
    
    def add_avto(self,new_avto):
        """Avtosalonga yangi avtolar qo'shish"""
        self.sotuvdagi_avtolar += new_avto 
    
    def get_info(self):
        """Salon haqida ma'lumotlar"""
        return f"Avtosalon nomi: {self.salon_nomi} manzili: {self.manzili} Sotuvdagi avtolar: \
{self.sotuvdagi_avtolar}"
        
    def see_methods(klass):
        return [method for method in dir(klass) if method.startswith("__") is False]
salon1 = Avtosalon("Billur", "Navoiy shahri", "Cobalt, Lacetti, Spark ")
print(see_methods(salon1))

print(salon1.__dict__)
print(salon1.__dict__.keys())

print(dir(str))
print(dir(int))
print(dir(print))
print(dir(dict))
print(dir(list))        

        
        
        