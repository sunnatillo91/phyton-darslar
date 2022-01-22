"""
Created on Wed Jan 19 08:52:38 2022

 
"""

# .items() METODI

talaba = {
    'ism': 'alijon',
    'familiya' : 'shamshiev',
    'yosh' : 22,
    'fakultet': 'matematika',
    'kurs' : 4
    }
print(talaba.items())

# barcha elementlarni tushunarliroq ifodalash uchun for siklidan foydalanamiz
for kalit, qiymat in talaba.items():
    print(f"Kalit: {kalit}")
    print(f"Qiymat: {qiymat}")
    
telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310'
    }

for k, q in telefonlar.items():
    print(f"{k.title()}ning telefoni {q}")
    
# .keys() METODI
maxsulotlar = {  # Do'kondagi maxsulotlar
    'olma':10000,
    'anor':20000,
    'uzum':40000,
    'anjir':25000,
    'shaftoli':30000
    }    
print(maxsulotlar.keys())

# print("Do'kondagi maxsulotlar:")
# for maxsulot in maxsulotlar.keys():
#     print(maxsulot.title())
  
print("Do'kondagi maxsulotlar:")
for maxsulot in maxsulotlar:
    print(maxsulot.title())    
    
# Ro'yxat va lug'at
bozorlik = ['anor','uzum','non','baliq']
for m in maxsulotlar:
  if m in bozorlik:    
    print(f"{m.title()} {maxsulotlar[m]} so'm")
    
for buyum in bozorlik:
  if buyum not in maxsulotlar:
      print(f"Kechirasiz, bizda {buyum} yo'q")

# Lug'at elementlarini tartib bilan chiqarish

print("Dp'konimizdagi maxsulotlar:")
for maxsulot in sorted(maxsulotlar):
   print(maxsulot.title())

#.values METODI

telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310'
    }
print(telefonlar.values())
print('Foydalanuvchilarning telefonlari:')
for tel in telefonlar.values():
    print(tel)
    
telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310',
    'hamida':'galaxy s9',
    'maryam':'huawei p30',
    'tohir':'iphone x',
    'umar':'iphone x'    
    }    
print('Foydalanuvchilarning telefonlari:')
for tel in telefonlar.values():
    print(tel)
    
# bir xil nomli maxsulotlar takrorini oldini olish uchun set() metodidan foydalanamiz   
print('Foydalanuvchilarning telefonlari:')
for tel in set(telefonlar.values()):
    print(tel)    

toys = {'ball','car','lamp','bear','car'}
type(toys)
print(toys) 
 
# Amaliyot

# Python izohli lug'atini yarating va lug'atga kamida 10 ta so'z qo'shing. Lug'atdagi har bir kalit va
#  qiymatni for tsikli yordamida, alifbo ketma-ketligida chiroyli qilib konsolga chiqaring. 
lugat = {
    'boolean':'mantiqiy qiymatlar',
    'in':'ro\'yxat tarkibida ma\'lum bir element borligini tekshiradi',
    'len()':'ro\'yxat uzunligini tekshirish',
    'list':'ro\'yxat',
    '.items()':'elementlar',
    'sorted()':'tartiblangan',
    '.keys()':'lug\'atdagi kalit so\'zlarnni topishda foydalaniladi',
    '.values()':'lug\'atdagi qiymatlarnni topishda foydalaniladi',
    'if':'agar',
    'and':'ikki va undan ko\'p shartlarning hammasi bajarilishini tekshiradi'
    }
print("Phython izohli lug'ati:")
for key, value in lugat.items():
    print(f"{key} - {value}")
    
# Davlatlar va ularning poytaxtlari lug'atini tuzing. Avval lug'atdagi davlatlarni, keyin poytaxtlarni 
# alohida-alohida, alifbo ketma-ketligida konsolga chiqaring. 
    
dav_poy = {
    "o'zbekiston":'toshkent',
    'qozog\'iston':'nursulton',
    'qirg\'iziston':'bishkek',
    'tojikiston':'Dushanbe',
    'turkmaniston':'Ashxobod',
    'turkiya':'istanbul',
    'germaniya':'berlin',
    'aqsh':'washington d.c.',
    'koreya':'seul'
    }
# print("Davlatlar ro'yxati':")
# for davlat in sorted(dav_poy.keys()):
#     print(davlat.title())
    
# print("Davlatlar poytaxtlari:")
# for poytaxt in sorted(dav_poy.values()):
#    print(poytaxt.title())
    
# # Foydalanuvchidan istalgan davlatni kiritishni so'rang va shu davlatning poytaxtini konsolga chiqaring.
# # Agar foydalanuvchi lug'atda yo'q davlatni kiritsa, "Bizda bunday ma'lumot yo'q" degan xabarni chiqaring.

# davlat1 = input("Istalgan davlat nomini kiriting: ").lower()
# poytaxt = dav_poy.get(davlat1, "Bizda bunday ma'lumot yo'q")
# print(poytaxt.upper())
    
# country = input("Qaysi davlat poytaxtini bilishni istaysiz? ").lower()
# capital = dav_poy.get(country)  
# if capital == None:
#     print("Bizda bunday ma'lumot yo'q")
# else:
#     print(f"{country.upper()} ning poytaxti, {capital.title()} shahri")    

# Restoran menusi lug'atini tuzing (kamida 10 ta taom-narh juftligini kiriting). Foydalanuvchidan 3 ta 
# ovqat buyurtma berishni so'rang. Foydalanuvchi kiritgan taomlarni menu bilan solishtiring, agar taom
# menuda bo'lsa narhini ko'rsating, aks holda "bizda bunday taom yo'q" degan xabarni chiqaring.

menu = {
        'osh':70000,
        'shashlik':60000,
        'baliq':80000,
        'jiz':100000,
        'lavash':25000,
        'tabaka':40000,
        'somsa':10000,
        'halisa':40000,
        'kfc':50000,
        'doner':20000
        }
buyurtma = []
for n  in range(3):
    buyurtma.append(input(f"{n+1}-ovqat tanlang:"))
for taom in buyurtma:
    if taom in menu:
       print(f"{taom.title()} {menu[taom]} so'm")
    else:
       print(f"Bizda {taom} yo'q")
       
       
    
   
    