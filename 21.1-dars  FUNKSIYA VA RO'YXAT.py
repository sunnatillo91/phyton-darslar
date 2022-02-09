"""
Created on Thu Feb  3 22:30:36 2022

Dasturlash asoslari

21.1-dars  FUNKSIYA VA RO'YXAT
                    
@author: Sunnatillo Xayrullayev
"""

# FUNKSIYA VA RO'YXAT

# def bahola(ismlar):
#     baholar = {}
#     while ismlar:
#         ism = ismlar.pop()
#         baho=input(f"{ism.title()}ning bahosini kiriting: ")
#         baholar[ism]=baho
#     return baholar
   
# talabalar = ['ali','vali','hasan','husan']
# baholar = bahola(talabalar)
# print(baholar)    

# RO'YXATGA O'ZGARTIRISH KIRITISH

# talabalar = ['ali','vali','hasan','husan']
# baholar = bahola(talabalar)
# print(talabalar)

# ASL RO'YXATGA O'ZGARTIRISH KIRITISHNING OLDINI OLISH
# Agar funksiya asl ro'yxatga o'zgartirish kiritishini istamasangiz, funksiyaga ro'yxatning o'zini emas, 
# uning nusxasini uzatish mumkin. Buning uchun funksiya parametrini royxat_nomi[:] ko'rinishida yozish kifoya. 
# Bunda [:] operatori ro'yxatdan nusxa olishni bildiradi:
    
# talabalar = ['ali', 'vali', 'hasan', 'husan']
# baholar = bahola(talabalar[:])
# print(talabalar)    

# AMALIYOT

# Matnlardan iborat ro'yxat qabul qilib, ro'yxatdagi har bir matnning birinchi harfini katta harfga
#  o'zgatiruvchi funksiya yozing. 

# def bosh_harf(ismlar):
#     for ism in range(len(ismlar)):
#         ismlar[ism] = ismlar[ism].title()

# names = ['ali','vali','hasan','husan']
# bosh_harf(names)
# print(names)


# Yuoqirdagi funksiyani asl ro'yxatni o'zgartirmaydigan va yangi ro'yxat qaytaradigan qilib o'zgartiring       
def bosh_harf(ismlar):
    ismlar = ismlar[:]
    for ism in range(len(ismlar)):
        ismlar[ism] = ismlar[ism].title()
    return ismlar

names = ['ali','vali','hasan','husan']
new_names = bosh_harf(names)
bosh_harf(names)
print(names)
print(new_names)

# Darsimiz davomida yozgan bahola funksiyasini .pop() metodidan foydalanmasdan va asl ro'yxatga o'zgartirish
# kiritmasdan faqat lug'at qaytaradigan qilib yozing.

def bahola(ismlar):
    baholar = {}
    while ismlar:
        ism = ismlar.pop() 
        baho=input(f"{ism.title()}ning bahosini kiriting: ")
        baholar[ism]=baho
    return baholar
   
talabalar = ['ali','vali','hasan','husan']
baholar = bahola(talabalar)
print(baholar)    