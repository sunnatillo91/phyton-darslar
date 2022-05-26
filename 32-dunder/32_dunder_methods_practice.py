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
    def __init__(self, nomi):
        self.nomi = nomi
        self.talabalar = []
        
    def add_student(self, *qiymat):
        for talaba in qiymat:
            if isinstance(talaba, Talaba):
                self.talabalar.append(talaba)
            else:
                print("Talaba obyektini kiriting")         
    
    def __getitem__(self, index):
        return self.talabalar[index]
    
    def __setitem__(self, index, qiymat):
        self.talabalar[index] = qiymat
    
    def __len__(self):
        return len(self.talabalar)
    
    def __add__(self, *qiymat):
        if isinstance(qiymat, Fan): 
            yangi_fan = Fan(f"{self.nomi} {qiymat.nomi}")
            yangi_fan.talabalar = self.talabalar + qiymat.talabalar
            return yangi_fan
        elif isinstance(qiymat, Talaba):
            self.add_student(qiymat)        
        else:
            print(f"Fan ga {type(qiymat)} qo'shib bo'lmaydi")
            
    def __repr__(self):
        return f"Fan: {self.nomi}"
    
    def __call__(self, *param):
        if param:
            for talaba in param:
                self.add_student(talaba)
        else:
            return [talaba for talaba in self.talabalar]


fan1 = Fan("Matematika")
fan2 = Fan("Astronomiya")

talaba1 = Talaba("Olim", "Hayitov", "AC4564652", 1995, 654897, 4)
talaba2 = Talaba("Salim", "Sharipov", "AC4564543", 1998, 657897, 3)
talaba3 = Talaba("Mehridin", "Boymonov", "AB4532543", 1992, 448897, 2)

fan2.add_student(talaba1)
# for talaba in [talaba1, talaba2]:
#     fan2.add_student(talaba)
    
# fan2[0] = Talaba("Mehriddin", "Boymonov", "AB456532", 1992, 336655)
print(fan2[0])
    
fan1.add_student(talaba1, talaba2, talaba3)
fan3 = fan1+fan2
print(fan3)
        