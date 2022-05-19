# -*- coding: utf-8 -*-
"""
Created on Thu May 12 20:17:49 2022

#32-DARS. DUNDER METODLAR AMALIYOT

Author: Sunnatillo Xayrullayev
"""


class Shaxs:
    """Shaxs klassi"""
    def __init__(self, ism, familiya, pasport, tyil):
        self.ism = ism
        self.familiya = familiya
        self.pasport = pasport
        self.tyil = tyil
        
    def __repr__(self):
        return f"{self.ism} {self.familiya}"
  
class Talaba(Shaxs):
    """Talaba klassi"""
    def __init__(self, ism, familiya, pasport, tyil, id, bosqich = 1):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, pasport, tyil)
        self.idraqam = id
        self.bosqich = bosqich
        
    def get_id(self):
        """Talabaning id raqami"""
        return self.idraqam
    
    def get_bosqich(self):
        """Talabaning bosqichi"""
        return self.bosqich
    
    def __lt__(self, boshqa_talaba):
        """Kichik"""
        return self.bosqich < boshqa_talaba.bosqich
    
    

shaxs = Shaxs("Hasan", "Olimov", "AB456123", 1998)

talaba1 = Talaba("Karim", "Nabiyev", "AC4656321", 1991, 45356, 3)
talaba2 = Talaba("Qobil", "Halimov", "AC4656123", 1998, 32562, 2)
print(talaba1>talaba2)

class Fan:
    """Fan klassi"""
    def __init__(self, fan_nomi, )

