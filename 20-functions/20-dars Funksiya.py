# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 11:35:49 2022

Dasturlash asoslari

20-dars Funksiya
                    
@author: Sunnatillo Xayrullayev
"""

# def salom_ber():
#     """Salom beruvchi funksiya"""
#     print("Assalomu alaykum!")
# salom_ber()

def salom_ber(ism):
    """Foydalanuvchiga salom beruvchi funksiya"""  # <- Docstring
    print(f"Assalomu alaykum, hurmatli {ism.title()}!")
salom_ber('hasan')    
salom_ber('olim')
print(print.__doc__)

# Murakkab funksiyalarda docstringni bir necha qatorga bo'lib yozish mumkin

def salom_ber(ism):
    """Foydalanuvchi ismini qabul qilib,
    unga salom beruvchi funksiya"""
    print(f"Assalomu alaykum, hurmatli {ism.title()}!")
    
# Docstringni konsolga chiqaruvchi buyruq quyidagicha:

# print(funksiya_nomi.__doc__)
# print()    

# Argument va parametr

# Funksiya yaratishda, qavs ichida berilgan, funksiya to'g'ri ishlashi uchun uzatiladigan qiymat parameter deb
#  ataladi. Yuqoridagi misolda ism bu salom_ber funksiyasining parametri. 
# Foydalanuvchi funksiyaga murojat qilishda funksiyaga uzatgan qiymat esa argument deb ataladi. 
# salom_ber('hasan') kodida 'hasan' bu argument. 

# FUNKSIYAGA BIR NECHTA ARGUMENT UZATISH
# To'g'ri tartibda uzatish

def toliq_ism(ism, familiya):
    """Ism va familiyani jamlab chiqaruvchi funksiya"""
    print(f"Foydalanuvchi ismi: {ism.title()}\n"
          f"Foydalanuvchi familiyasi: {familiya.title()}")
    
toliq_ism('olim', 'hakimov')

# Agar argumentlarni noto'g'ri ketma-ketlikda berilsa natija noto'g'ri chiqadi

toliq_ism('hakimov', 'olim')    

#  Ko'p hollarda argumentlarni noto'g'ri tartibda uzatish xatolikka ham olib kelishi mumkin

def yosh_hisobla(ism, tugilgan_yil):
    """Foydalanuvchi yoshini hisoblaydigan funksiya""" 
    print(f"{ism.title()} {2022-tugilgan_yil} yoshda")

yosh_hisobla('olim', 1997)

# Endi argumentlarni o'rnini almashtirib yozib ko'ramiz:
# yosh_hisobla(1997, 'olim')    
#AttributeError: 'int' object has no attribute 'title'

# Parametr nomi bilan uzatish

yosh_hisobla(tugilgan_yil=1997, ism='olim')

toliq_ism(familiya='hakimov', ism='olim')

# STANDART QIYMAT

def yosh_hisobla(tugilgan_yil, joriy_yil=2022):
    """Tug'ilgan yildan yoshni hisoblaymiz"""
    print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")
yosh_hisobla(1991,2022)
yosh_hisobla(1991)

# FUNKSIYAGA MUROJAAT ETISHDA XATOLIKLAR
#1
# def yosh_hisobla(tugilgan_yil, joriy_yil=2022):
#     """Tug'ilgan yildan yoshni hisoblaymiz"""
#     print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")
# tyil = int(input("Tug'ilgan yilingizni kiriting: "))
# yosh_hisobla(tyil)

#2

# def yosh_hisobla(tugilgan_yil, joriy_yil):
#     """Tug'ilgan yildan yoshni hisoblaymiz"""
#     print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")    
# yosh_hisobla(1993,2022)  

# #3
# def salom_ber():
#     """Salom beruvchi funksiya"""
#     print("Assalomu alaykum!")
# salom_ber()

# #4
# def toliq_ism(ism, familiya):
#     print(f"Foydalanuvchi ismi: {ism.title()}\n"
#           f"Foydalanuvchi familiyasi: {familiya.title()}")
    
# toliq_ism('olim', 'hakimov')

# AMALIYOT
# 1 Foydalanuvchi ismi va yoshini so'rab, uning tug'ilgan yilini hisoblaydigan funksiya yozing.
def tugilgan_yil(ism, yosh, joriy_yil=2022):
    """Foydalanuvchi ismi va yoshini so'rab, uning tug'ilgan yilini hisoblaydigan funksiya"""
    print(f"{ism.title()}, siz {joriy_yil-yosh} - yilda tug'ilgansiz")
tugilgan_yil('sunnatillo', 31)    

# 2 Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi funksiya yozing.

def kvadrat_kub(son):
    """Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi funksiya"""
    print(f"{son} ning kvadrati {son**2}, {son} ning kubi esa {son**3} ga teng")
kvadrat_kub(-1.5)

# 3 Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi funksiya yozing.

# def juft_toq(son):
#     """Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi funksiya"""
#     if son%2==0 and son>0:
#        print(f"{son} juft son")
#     elif son%2!=0 and son>0:
#        print(f"{son} toq son")
#     else:
#        print("Butun musbat son kiriting: ")
# son = int(input("son kiriting"))       
# juft_toq(son)

# 4 Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi funksiya yozing. Agar sonlar
# teng bo'lsa "Sonlar teng" degan xabarni chiqaring.
def katta_son(x, y):
    """Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi funksiya"""
    if x>y:
        print(f"Ikkita sondan kattasi {x}")
    elif x<y:
        print(f"Ikkita sondan kattasi {y}")
    else:
        print(f"Sonlar teng: {x} = {y}")
katta_son(5, 5)

# 5 Foydalanuvchidan x va n sonlarini olib, x ning n-darajasini konsolga chiqaruvchi funksiya yozing.
def daraja_hisob(x, n):
    """Foydalanuvchidan x va n sonlarini olib, x ning n-darajasini konsolga chiqaruvchi funksiya"""
    print(f"{x} ning {n} - darajasi {x**n} ga teng")
daraja_hisob(5, 4)    

# 6 Yuqoridagi funksiyada y uchun 2 standart qiymatini bering.
def daraja_hisob(x, y=2):
    """Foydalanuvchidan x va n sonlarini olib, x ning n-darajasini konsolga chiqaruvchi funksiya"""
    print(f"{x} ning {y} - darajasi {x**y} ga teng")
daraja_hisob(5)    

# 7 Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo'lgan sonlarga qoldiqsiz bo'linishini 
# tekshiruvchi funksiya yozing. Natijalarni konsolga chiqaring.
    
def bolinish_alomatlari(son):
    """Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo'lgan sonlarga qoldiqsiz bo'linishini,
    tekshiruvchi funksiya"""
    for n in range(2,11):
        if son%n==0:
            print(f"{son} {n} ga qoldiqsiz bo'linadi")
bolinish_alomatlari(120)           
bolinish_alomatlari(12)            
bolinish_alomatlari(-48)
