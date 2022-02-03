"""
Created on Sun Jan 30 11:00:30 2022

Dasturlash asoslari

21-dars  QIYMAT QAYTARUVCHI FUNKSIYA
                    
@author: Sunnatillo Xayrullayev
"""
# Funksiyadan yagona qiymat qaytarish
# def toliq_ism_yasa(ism, familiya):
#     """Toliq ism qaytaruvchi funksiya"""
#     toliq_ism = f"{ism} {familiya}"
#     return toliq_ism.title()
# talaba1 = toliq_ism_yasa('olim', 'hakimov')
# talaba2 = toliq_ism_yasa('hakim', 'olimov')
# print(f"Darsga kelmagan talabalar {talaba1} va {talaba2}")

# # Ixtiyoriy argumentlar

# def toliq_ism_yasa(ism, familiya, otasining_ismi=''):
#     """Toliq ism qaytaruvchi funksiya"""
#     if otasining_ismi:  # Otasining ismi mavjud bo'lsa
#         toliq_ism = f"{ism} {otasining_ismi} {familiya}"
#     else:
#         toliq_ism = f"{ism} {familiya}"
#     return toliq_ism.title()
# toliq_ism_yasa('saidov', 'karim', 'halimovich')
    
# talaba1 = toliq_ism_yasa('olim', 'hakimov')
# talaba2 = toliq_ism_yasa('hakim', 'olimov', 'abrorovich')
# print(f"Darsga kelmagan talabalar {talaba1} va {talaba2}")

# Funksiyadan lug'at qaytarish

# def avto_info(make, model, rangi, korobka, yili, narxi=None):
#     avto = {'kompaniya':make,
#             'model':model,
#             'rangi':rangi,
#             'korobka':korobka,
#             'yil':yili,
#             'narx':narxi
#             }
#     return avto

# avto1 = avto_info('GM', 'Malibu', "Qora", 'Avtomat', 2018)
# avto2 = avto_info('GM', 'Gentra', 'Qora', "Avtomat", 2021)
# avtolar = [avto1, avto2]
# print('Onlayn bozordagi avtomashinalar:')
# for avto in avtolar:
#     if avto['narx']:
#         narx = avto['narx']
#     else:
#         narx = "Noma'lum"
#     print(f"{avto['rang']} {avto['model']}. Narxi: {narx}")            
    
# Funksiyadan ro'yxat qaytaramiz

# def oraliq(min, max):
#      sonlar = []   # bo'sh ro'yxat
#      while min<max:
#          sonlar.append(min)
#          min+=1
#      return sonlar
# print(oraliq(0,10))
# print(oraliq(10,21))   

# Yuqoridagi funksiyaga uchinchi, qadam deb nomlangan ixtiyoriy parameterni qo'sha olasizmi?
# def oraliq(min, max, qadam=1):
#       sonlar = []   # bo'sh ro'yxat
#       while min<max:
#           sonlar.append(min)
#           min+=qadam
#       return sonlar
# print(oraliq(0,21,4))
# print(oraliq(10,21,4))           

# Funksiyalarni siklda ishlatish

# print("Saytimizdagi avtolar ro'yxatini shakllantiramiz.")
# avtolar=[]  # Salondagi avtolar uchun bo'sh ro'yxat
# while True:
#     print("\nQuyidagi ma'lumotlarni kiriting", end='')
#     kompaniya=input("Ishlab chiqaruvchi: ")
#     model=input("Modeli: ")
#     rangi=input("Rangi: ")
#     korobka=input("Korobka: ")
#     yili=input("Yili: ")
#     narxi=input("Narxi: ")
#     #Kiritilgan ma'lumotlardan avto_info yordamida 
#     #lug'at shakllantirib ro'yxatga qo'shamiz:
#     avtolar.append(avto_info(kompaniya, model, rangi, \
#                               korobka, yili, narxi))
        
#         # Yana avto qo'shish qo'shmaslikni so'raymiz
#     javob=input("Yana avto qo'shasizmi? (yes/no): ")
#     if javob=='no':
#         break    
    
# print("\nSalonimizdagi avtolar: ")
# for avto in avtolar: 
#     if avto["narx"]:
#         narx = avto['narx']
#     else:
#         narx = "Noma'lum"
#     print(
#       f"{avto['rangi'].title()} {avto['model'].title()}, {avto['korobka']} korobka. Narxi: {narxi} ")    
        
    
# AMALIYOT

# Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, email manzili va telefon raqamini 
# qabul qilib, lug'at ko'rinishida qaytaruvchi funksiya yozing. Lug'atda foydalanuvchu yoshi ham bo'lsin.
#  Ba'zi argumentlarni kiritishni ixtiyoriy qiling (masalan, tel.raqam, el.manzil)
# def user_info(ism, familiya, tyil, tjoy, yosh, email=None, tel=None):
#     """Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, email manzili va telefon raqamini,
#     qabul qilib, lug'at ko'rinishida qaytaruvchi funksiya"""
#     malumot = {
#         'ism' : ism,
#         'familiya':familiya,
#         'tyil':tyil,
#         'tjoy':tjoy,
#         'email':email,
#         'tel':tel,
#         'yosh':yosh,
#         }
#     return malumot

# print(user_info('olim', 'halimov', 1991, 'samarqand', 31))
        
        
# Yuqoridagi funksiyani while yordamida bir necha bor chaqiring, va mijozlar degan ro'yxatni shakllantiring. 
# Ro'yxatdagi mijozlar haqidagi ma'lumotni konsolga chiqaring.
# mijozlar = []
# while True:
#     print("\nQuyidagi ma'lumotlarni kiriting:",end='')
#     ism=input("Ismi: ")
#     familiya=input("Familliya: ")
#     tyil=input("Tug'ilgan yili: ")
#     tjoy=input("Tug'ilgan joyi: ")
#     email=input("Emaili: ")
#     tel=input("Teleefon raqami: ")
#     yosh=input("Yoshi: ")    
#     yosh=int(yosh)
#     mijozlar.append(user_info(ism, familiya, tyil, tjoy, yosh))
    
#     javob = input("Yana ma'lumot qo'shasizmi? (yes/no): ")
#     if javob == 'no':
#         break
    
# print("\Mijozlar haqidagi ma'lumotlar: ")
# for mijoz in mijozlar:
#     if mijoz["email"]:
#         email=mijoz["email"]
#     if mijoz["tel"]:
#         tel=mijoz["tel"]
#     else:
#         email='None'
#         tel='None'
# print(
#       f"{mijoz['ism'].title()} {mijoz['familiya'].title()} {mijoz['tyil']} yil {mijoz['tjoy'].title()}da\
# tug'ilgan. Yoshi {mijoz['yosh']}da. Elektron manzili: {mijoz['email']}, telefon raqami: {mijoz['tel']}.")        
    
# Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya yozing

# def katta_son(x, y, z):
#     """Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya"""
#     if x>y and x>z:
#         print(f"{x}>{y}, {x}>{z}")
#     elif y>x and y>z:
#         print(f"{y}>{x}, {y}>{z}")
#     else:    
#          print(f"{z}>{x}, {z}>{y}")
        
# print(katta_son(12, 21, -8))     
# katta_son(12, 21, 8)   
# katta_son(5, 8, 12)

# def kattasi(x,y,z):
#     max=x
#     if y>=max:
#         max=y
#     if z>=max:
#         max=z
#     return max    
# print(kattasi(5, 12, -47))
    
# Foydalanuvchidan aylaning radiusini qabul qilib olib, uning radiusini, diametrini, perimetri va yuzini 
# lug'at ko'rinishida qaytaruvchi funksiya yozing
def aylana_info(r, pi=3.14159):
    aylana = {
        'radius':r,
        'diametr':2*r,
        'perimetr':2*pi*r,
        'yuzi':pi*r**2        
        }
    return aylana
aylana_info(7)
print(aylana_info(7))

# Berilgan oraliqdagi tub sonlar ro'yxatini qaytaruvchi funksiya yozing (tub sonlar —faqat birga va o'ziga
#  qoldiqsiz bo'linuvchi, 1 dan katta musbat sonlar)

def tub_son(min,max):
    tub_sonlar = []
    for n in range(min, max+1):
        tub = True
        if n == 1:
            tub = False
        elif n==2:
            tub = True
        else:
            for x in range(2, n):
                if n%x == 0:
                    tub = False
        if tub:
            tub_sonlar.append(n)
    return tub_sonlar
    
print(tub_son(2, 45))
      
# Foydalanuvchidan son qabul qilib, shu son miqdoricha Fibonachchi ketma-ketligidagi sonlar ro'yxatni 
# qaytaruvchi funksiya yozing.  Ta’rif: Har bir hadi o’zidan oldingi ikkita hadning yig’indisiga teng 
# bo’lgan ketma-ketlik Fibonachchi ketma-ketligi deyiladi. Bunda boshlang’ish had ko’pincha 1 deb olinadi. 
#  1, 1, 2, 3, 5, 8, 13, 21, 34, 55,...


def febonachchi(n):
    """Foydalanuvchidan son qabul qilib, shu son miqdoricha Fibonachchi ketma-ketligidagi sonlar ro'yxatni 
qaytaruvchi funksiya"""
    sonlar = []
    for x in range(n):
       if x==0 or x==1:
          sonlar.append(1)
       else:
          sonlar.append(sonlar[x-1]+sonlar[x-2])
    return sonlar
        
print(febonachchi(20))