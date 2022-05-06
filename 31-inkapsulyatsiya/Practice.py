"""
Created on Wed May  4 08:40:01 2022

Dasturlash asoslari

31_lesson INKAPSULYATSIYA, AMALIYOT

Author: Sunnatillo Xayrullayev
"""

# Avvalgi darslarimizda yaratgan Shaxs va Talaba klasslariga yopiq xususiyatlar qo'shing 
# va ularning qiymatini ko'rsatuvchi va o'zgartiruvchi metodlar yozing.

class Shaxs:
    __jinsi = "erkak/ayol"
    __num_shaxs = 0
    """Shaxslar haqida ma'lumot"""
    def __init__(self, ism, familiya, pasport, tyil):
        self.ism = ism
        self.familiya = familiya
        self.pasport = pasport
        self.tyil = tyil
        Shaxs.__jinsi = "erkak/ayol"
        Shaxs.__num_shaxs += 1
        
    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}."
        info += f" Pasport: {self.pasport}, {self.tyil}-yilda tug'ilgan"
        return info
    
    def get_age(self, yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil-self.tyil
    
    @classmethod
    def get_jinsi(cls):
        return cls.__jinsi
    
    @classmethod
    def get_num_shaxs(cls):
        return cls.__num_shaxs
    
inson = Shaxs("Hasan", "Salomov", "AC123456", 1996)
print(f"{inson.get_info()}. {inson.get_age(2022)} yoshda.")

print(Shaxs.get_num_shaxs())



class Talaba(Shaxs):
    __talabalar_soni = 0
    """Talaba klassi"""
    def __init__(self, ism, familiya, pasport, tyil, id, manzil):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, pasport, tyil)
        self.idraqam = id
        self.bosqich = 1
        self.manzil = "manzil"
        self.fanlar = []
        Talaba.__talabalar_soni += 1
                
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
    
    @classmethod
    def get_talabalar_soni(cls):
        return cls.__talabalar_soni
    
talaba = Talaba("Abror", "To'laganov", "AB321456", 1995, "008356", "manzil")
print(Talaba.get_talabalar_soni())