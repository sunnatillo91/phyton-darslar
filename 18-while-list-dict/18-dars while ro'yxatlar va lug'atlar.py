"""
Created on Mon Jan 24 20:14:49 2022
Dasturlash asoslari

18-dars while ro'yxatlar va lug'atlar bilan ishlash
                    
@author: Sunnatillo Xayrullayev
"""

# while yordamida ro'yxatni to'ldirish

# ismlar = []
# print("Yaqin do'stlaringiz ro'yxatini tuzamiz")
# n=1  # ismlarni sanash uchun
# while True:
#     savol = f"{n}-do'stingiz ismini kiriting: "
#     ism= input(savol)
#     ismlar.append(ism)
#     javob = input("Yana ism qo'shasizmi? (ha/yo'q) ")
#     if javob == 'ha':
#         n+=1
#         continue
#     else:
#         break
# print("Ro'yxat tuzildi")
# print("Do'stlaringiz ro'yxati: ")
# for ism in ismlar:
#     print(ism.title())

# while yordamida lug'atni to'ldirish
    
# print("Do'stlaringiz yoshini saqlaymiz.")
# dostlar = {}
# ishora = True 
# while ishora:
#     ism=input("Do'stingiz ismini kiriting: ")
#     yosh = input(f"{ism.title()}ning yoshini kiriting: ")
#     dostlar[ism] = int(yosh)  # ism kalit, yosh qiymat
    
#     javob = input("Yana ma'lumot qo'shasizmi? (ha/yo'q)")
#     if javob == "yo'q":
#         ishora = False
        
# for ism, yosh in dostlar.items():
#     print(f"{ism.title()} {yosh} yoshda")
    
# Ro'yxat elementlarini o'chirish
    
# cars = ['lacetti','nexia','toyota','nexia','malibu','nexia']
# while 'nexia' in cars:
#     cars.remove('nexia')
# print(cars)    

# # Ro'yxatdan ro'yxatga element ko'chirish    
    
# talabalar = ['hasan','husan','olim','botir']
# baholangan_talabalar = {}
# while talabalar:
#     talaba = talabalar.pop()
#     baho = input(f"{talaba.title()} ning bahosini kiriting: ")
#     print(f"{talaba.title()} baholandi")
#     baholangan_talabalar[talaba] = baho
    
# AMALIYOT

#1 Foydalanuvchidan buyurtma qabul qiluvchi dastur yozing. Mahsulotlar nomini birma-bir qabul qilib, yangi
# ro'yxatga joylang.
# buyurtmalar = []
# print("Buyurtmalaringiz ro'yxatini tuzamiz: ")
# n = 1
# while True:
#     savol = f"{n}-buyurtmangizni kiriting: "
#     buyurtma = input(savol)
#     buyurtmalar.append(buyurtma)
#     javob = input("Yana buyurtma qo'shasizmi? (ha/yo'q) ")
#     if javob == 'ha':
#         n += 1
#         continue
#     else:
#         break
# print(f"Ro'yxat tuzildi: {buyurtmalar}") 
 
# e-bozor uchun mahsulotlar va ularning narhlari lug'atini shakllantiruvchi dastur yozing. Foydalanuvchidan 
# lug'atga bir nechta elementlar (mahsulot va uning narhi) kiritishni so'rang.

# e_bozor = {}
# ishora = True
# while ishora:
#     maxsulot = input("e_bozor uchun maxsulot nomini kiriting: ")
#     narx = input("e_bozor uchun maxsulot narxini kiriting: ")
#     e_bozor[maxsulot] = int(narx)
    
#     javob = input("Yana maxsulot qo'shasizmi? (ha/yo'q) ")
#     if javob == "yo'q":
#         ishora = False
# for maxsulot, narx in e_bozor.items():
#     print(f"{maxsulot} ning narxi {narx} so'm")    
    

# Yuqoridagi ikki dasturni jamlaymiz. Foydalanuvchi buyurtmasi ro'yxatidagi har bir mahsulotni e-bozordagi 
# mahsulotlar bilan solishitiring (tayyor ro'yxat ishlatishingiz mumkin). Agar mahsuot e-bozorda mavjud bo'lsa 
#  mahuslot narhini chiqaring, aks holda "Bizda bu mahsulot yo'q" degan xabarni kor'sating.
buyurtmalar = ['olma','uzum','non','tuz']
maxsulotlar = {
    'olma':10000,
    'mayiz':27000,
    'non':3000,
    'tuz':2000,
    'shakar':8000
    }

while buyurtmalar:
    buyurtma = buyurtmalar.pop() 
    if buyurtma in maxsulotlar.keys():
        narx = maxsulotlar[buyurtma]
        print(f"{buyurtma.title()} - {narx} so'm")
    else:
        print(f"{buyurtma} bizda yo'q")
    