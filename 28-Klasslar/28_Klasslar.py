# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 20:44:48 2022

Dasturlash asoslari

28-dars KLASSLAR

Author: Sunnatillo Xayrullayev

"""

# x=10
# print(type(x))

# # KLASS YARATISH

# class Talaba:
#     """Talaba nomli klass yaratamiz"""
#     def __init__(self,ism,familiya,tyil):
#         """Talabaning xususiyatlari"""
#         self.ism=ism
#         self.familiya=familiya
#         self.tyil=tyil
       
# # Klassdan obyekt yaratish
        
# talaba1=Talaba("Alijon",'Valiyev', 1993)
               
# # Obyekttningg xususiyatlarini ko'rish

# print(talaba1.ism)        
# print(talaba1.tyil) 

# # Klassdan bir nechta obyektlar yaratish

# talaba2=Talaba("Olim",'Aliyev',1999)
# talaba3=Talaba("Valijon",'Soliyev',2000)
# talaba4=Talaba("Akrom",'Choriqulov',1991)
# print(talaba3.ism)

# # Klassga metodlar qo'shamiz

# class Talaba:
#     """Talaba nomli klass yaratamiz"""
#     def __init__(self,ism,familiya,tyil):
#         """Talabaning xususiyatlari"""
#         self.ism=ism
#         self.familiya=familiya
#         self.tyil=tyil
        
#     def tanishtir(self):
#         return(f"Ismim {self.ism} familiyam {self.familiya}."
#             f"{self.tyil} yilda tug'ilganman")
        
# talaba4=Talaba("Akrom",'Choriqulov',1991)
# print(talaba4.tanishtir())

# class Talaba:
#     """Talaba nomli klass yaratamiz"""
#     def __init__(self,ism,familiya,tyil):
#         """Talabaning xususiyatlari"""
#         self.ism=ism
#         self.familiya=familiya
#         self.tyil=tyil
        
#     def get_name(self):
#         """Talabaning ismini qaytaradi"""
#         return self.ism
    
#     def get_lastname(self):
#         """Talabaning familiyasini qaytaradi"""
#         return self.familiya
    
#     def get_fullname(self):
#         """Talabaning ism-familiyasini qaytaradi"""
#         return f"{self.ism} {self.familiya}"
    
# talaba2=Talaba("Olim",'Aliyev',1999)    
# print(talaba2.get_fullname())    
# print(talaba2.get_lastname())    

# # Argument qabul qiluvchi metodlar

# class Talaba:
#     """Talaba nomli class yaratamiz"""
#     def __init__(self, ism,familiya,tyil):
#         """Talabaning xususiyatlari"""
#         self.ism=ism
#         self.familiya=familiya
#         self.tyil=tyil
        
#     def get_age(self, yil):
#         """Talabaning yoshini qaytaradi"""
#         return yil-self.tyil
    
# talaba2=Talaba("Olim",'Aliyev',1999)
# talaba3=Talaba("Valijon",'Soliyev',2000)
# talaba4=Talaba("Akrom",'Choriqulov',1991)

# print(talaba2.get_age(2022))

# pass operatori

# class User:
#     def __init__(self,name,username,email):
#         self.name=name
#         self.username=username
#         self.mail=email
        
#     def describe():
#         pass
    
#     def get_email():
#         pass

# Amaliyot

# Web sahifangiz uchun foydalanuvchi (user) klassini tuzing. Klassning xususiyatlari
# sifatida odatda ijtimoiy tarmoqlar talab qiladigan ma'lumotlarni kiriting (ism,
# foydalanuvchi ismi, email, va hokazo)
# class User:
#     def __init__(self,name,username,lastname,email,tyil):
#         self.name=name
#         self.lastname=lastname
#         self.username=username
#         self.mail=email
#         self.tyil=tyil
        
# user1=User("Sunnatillo", "Xayrullayev",'sunnat91','sunnatillo@mail.ru','1991') 
       
    
# Klassga bir nechta metodlar qo'shing, jumladan get_info() metodi foydalanuvchi 
# haqida yig'ilgan ma'lumotlarni chiroyli qilib chiqarsin (masalan: "Foydalanuvchi: 
# alijon1994, ismi: Alijon Valiyev, email: alijon1994@gmail.com).
class User:
    def __init__(self,name,username,lastname,email,tyil):
        self.name=name
        self.lastname=lastname
        self.username=username
        self.mail=email
        self.tyil=tyil
        
    def get_info(self):
        """Foydalanuvchining ma'lumotlarini qaytaradi"""
        return f"Foydalanuvchi: {self.username}, ismi: {self.name} {self.lastname},\
 email: {self.mail}"
    
      
user1=User("Sunnatillo",'sunnat91',"Xayrullayev",'sunnatillo@mail.ru','1991') 
print(user1.get_info())            

                                            
# Klassdan bir nechta obyektlar yarating va uning xususiyatlari va metodlariga 
# murojat qiling.
    
user2=User("Jahongir", "jahon91","Usmonov", "jahon91@gmail.com",1991)
user3=User("Baxrom","boxo92","Pulatov","pulatov@mail.ru",1993)

print(user2.lastname)
print(user1.mail)
print(user2.get_info())
print(user3.get_info())

        
       