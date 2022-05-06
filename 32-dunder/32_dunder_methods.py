# -*- coding: utf-8 -*-
"""
Created on Wed May  4 09:48:31 2022

Dasturlash asoslari

#32-DARS. DUNDER METODLAR

Author: Sunnatillo Xayrullayev
"""

class Avto:
    __num_avto = 0
    """Avtomobil klassi"""
    def __init__(self, make, model, rang, yil, narx):
        """Avtomobilning xususiyatlari"""
        self.make=make
        self.model=model
        self.rang=rang
        self.yil=yil
        self.narx=narx
        Avto.__num_avto +=1

# OBYEKT HAQIDA MA'LUMOT
        
    # def __str__(self):
    #     return f"Avto: {self.make} {self.model}"
    
    def __repr__(self):                                 # representation
        return f"Avto: {self.make} {self.model}"
    
    def __eq__(self, boshqa_avto):
        """Tenglik"""        
        return self.narx == boshqa_avto.narx
    
    def __lt__(self, boshqa_avto):
        """Kichik"""
        return self.narx < boshqa_avto.narx
    
    def __le__(self, boshqa_avto):
        """Kichik yoki teng"""
        return self.narx <= boshqa_avto.narx
   
    

    
avto1 = Avto("GM","Malibu","Qora",2020,40000)
print(avto1)

# OBYEKTLARNI TAQQOSLASH

x,y = 5,10
print(x>y)

avto1 = Avto("GM","Malibu","Qora",2020,40000)
avto2 = Avto("GM","Lacetti","Oq",2021,20000)
print(avto1>avto2)
avto3 = Avto("Honda","Accord","Oq", 2017, 40000)
print(avto2 == avto3)

# OBYEKT  UZUNLIGI

matn = "Hello world"
print(len(matn))

sonlar = [12, 45, 38, 49, 54]
print(len(sonlar))

class Avtosalon:
    """Avtosalon klassi"""
    def __init__(self, name):
        self.name = name
        self.avtolar = []
        
    def __repr__(self):
        return f"{self.name} avtosaloni"
    
    def __getitem__(self, index):
        return self.avtolar[index]
    
    def __setitem__(self, index, qiymat):
        if isinstance(qiymat, Avto):
            self.avtolar[index] = qiymat
    
    def add_avto(self, *qiymat):
        for avto in qiymat:
            if isinstance(avto, Avto):
                self.avtolar.append(avto)
            else:
                print("Avto kiriting")
                
    # def __add__(self, qiymat):
    #     if isinstance(qiymat, Avtosalon):
    #         yangi_salon = Avtosalon(f"{self.name} {qiymat.name}")
    #         yangi_salon.avtolar = self.avtolar + qiymat.avtolar
    #         return yangi_salon
        
    def __add__(self, qiymat):       #salonga yangi Avto qo'shish imkoni
        if isinstance(qiymat, Avtosalon):
            yangi_salon = Avtosalon(f"{self.name} {qiymat.name}")
            yangi_salon.avtolar =self.avtolar + qiymat.avtolar
            return yangi_salon
        elif isinstance(qiymat, Avto):
            self.add_avto(qiymat)
        else:
            print(f"Avtoosalonga {type(qiymat)} qo'shib  bo'lmaydi")
                
avto1 = Avto("GM","Malibu","Qora",2020,40000)
avto2 = Avto("GM","Lacetti","Oq",2021,20000)
avto3 = Avto("Honda","Accord","Oq", 2017, 40000)


    
salon1 = Avtosalon("MaxAvto")
print(salon1)

salon1.add_avto(avto1, avto2, avto3)

print(salon1[:])

# Obyekt elementini o'zgartirish uchun metod

avto4 = Avto("Tesla","X7","Oq", 2017, 45000)

print(salon1[0])
salon1[0] = avto4
print(salon1[0])


# OPERATORLARNI QAYTA TALQIN QILISH

x, y = 10, 20

print(x+y)
print(x*5)

# Matnlar

t1 = "Hello"
t2 = "world"
print(t1+t2)
print(t1*5)

# Ro'yxatlar

l1 = [1,2,3]
l2 = [3,4,5]
print(l1+l2)
print(l2*3)

salon1 = Avtosalon("MaxAvto")
salon2 = Avtosalon("Avto Lider")
avto1 = Avto("GM","Malibu","Qora",2020,40000)
avto2 = Avto("GM","Lacetti","Oq",2021,20000)
avto3 = Avto("Honda","Accord","Oq", 2017, 40000)
avto4 = Avto("Mazda","6","Qizil",2015,35000)
avto5 = Avto("Volkswagen","Polo","Qora",2020,30000)
avto6 = Avto("Toyota","Corola","Silver", 2018, 45000)
salon1.add_avto(avto1, avto2, avto3)
salon2.add_avto(avto4, avto5, avto6)


# Qo'shish operatorini qaytatalqin etish uchun Avtosalon klassimizga __add__ metodin qo'shamiz
 
salon3 = salon1 + salon2

print(salon3)
print(salon3[:])

# Qo'shish operatori yordamida salonga yangi Avto qo'shish imkonini ham yaratishimiz mumkin

avto7 = Avto("BMW","X7","Qora", 2015, 75000)
salon1+avto7
print(salon1[:])