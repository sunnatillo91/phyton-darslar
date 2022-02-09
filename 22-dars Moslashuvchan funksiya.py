
"""
Created on Tue Feb  8 16:08:59 2022

Dasturlash asoslari

22-dars MOSLASHUVCHAN FUNKSIYA
"""

# *args USULI 

# def summa(*sonlar):
#     """Kiritilgan sonlar yig'indisini qaytaruvchi funksiya"""
#     yigindi = 0
#     for son in sonlar:
#         yigindi += son
#     return yigindi

# print(summa(1,2,3))  

# print(summa(12,13,15,21))  

def summa(*sonlar):
    """Kiritilgan sonlar yig'indisini qaytaruvchi funksiya"""
    return sum(sonlar)
print(summa(4,5,6,7))

# Agar funksiya bir nechta qiymat qabul qilsa *args argumenti oxirida yoziladi
def summa(x,y,*sonlar):
    """Kiritilgan sonlar yig'indisini qaytaruvchi funksiya"""
    return x+y+sum(sonlar)
# print(summa(2))
# TypeError: summa() missing 1 required positional argument: 'y'

# print(summa(9, 10, 21))
# print(summa(10, -10))

# # *kwargs USULI

# # Agar funksiyaga kalit so'z - qiymat ko'rinishidagi argumentlarni uzatish talab qilinsa, va bunday parametrlar soni 
# # noma'lum bo'lsa, argument oldidan ikkita yulduzcha qo'yiladi (**kwargs).
# # **kwargs — keyword arguments (kalit so'zli argumentlar)

# def avto_info(kompaniya,model,**malumotlar):
#     """Avto haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
#     malumotlar['kompaniya']=kompaniya 
#     malumotlar['model']=model
#     return malumotlar

# avto1 = avto_info("GM", "malibu", rang = 'qora', yil=2018)
# avto2 = avto_info("kia", "K5", rang="qizil", yil=2019, narx=35000)
# print(avto2)
# print(avto1)

# Amaliyot

#Istalgancha sonlarni qabul qilib, ularning ko'paytmasini qaytaruvchi funksiya yozing

def kopaytmalar(*sonlar):
    """Kiritilgan sonlar ko'paytmasini hisoblovchi funksiya"""
    kopaytma = 1
    for son in sonlar:
        kopaytma *= son
    return kopaytma
    
print(kopaytmalar(5,12))

# Talabalar haqidagi ma'lumotlarini lug'at ko'rinishida qaytaruvchi funkisya yozing. Talabaning ismi va 
# familiyasi majburiy argument, qolgan ma'lumotlar esa ixtiyoriy ko'rinishda istalgancha berilishi mumkin bo'lsin.

def talaba_info(ism, familiya, **malumotlar):
    """Talabalar haqidagi ma'lumotlarini lug'at ko'rinishida qaytaruvchi funkisya"""
    malumotlar['ism']=ism
    malumotlar['familiya']=familiya
    return malumotlar

talaba1 = talaba_info("Salim", "Karimov", muassasa="NDKI", kurs=3, yonalish='konchilik ishi')
print(talaba1)