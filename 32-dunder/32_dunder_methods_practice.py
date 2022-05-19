# -*- coding: utf-8 -*-
"""
Created on Tue May 17 12:37:52 2022

Dasturlash asoslari

#32-DARS. DUNDER METODLAR AMALIYOT

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
    
    def __repr__(self):
        return f"{self.ism} {self.familiya}"
    
inson = Shaxs("O'tkir", "Varlamov", "AC123654", 1985)
print(inson)

class Talaba(Shaxs):
    """Talaba haqida ma'lumot"""
    def __init__(self, ism, familiya, passport, tyil, id, bosqich = 1):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)
        self.id = id
        self.bosqich = bosqich
        
    def __lt__(self, boshqa_talaba):
        """Kichik"""
        return self.bosqich < boshqa_talaba.bosqich
    
    def __ge__(self, boshqa_talaba):
        """Katta yoki teng"""
        return self.bosqich>=boshqa_talaba.bosqich
   
    def __repr__(self):
        return f"Talaba: {self.ism} {self.familiya}"
    
talaba1 = Talaba("Olim", "Hayitov", "AC4564652", 1995, 654897, 4)
talaba2 = Talaba("Salim", "Sharipov", "AC4564543", 1998, 657897, 3)
print(talaba1>talaba2)

class Fan:
    def __init__(self, nomi, dars_soati):
        self.nomi = nomi
        self.dars_soati = dars_soati
        self.talabalar = []
        
    def add_student(self, talaba):
        if isinstance(talaba, Talaba):
            self.talabalar.append(talaba)
        else:
            print("Talaba obyektini kiriting")
            
        
    def __getitem__(self):
        return f"{self.nomi} {self.dars_soati}"
    
    def __setitem__(self, yangi_soat):
        return f"{self.yangi_soat}"


talaba1 = Talaba("Olim", "Hayitov", "AC4564652", 1995, 654897, 4)
talaba2 = Talaba("Salim", "Sharipov", "AC4564543", 1998, 657897, 3)

math = Fan("matematika", 24)

talabalar.add_student(talaba1)
    
        