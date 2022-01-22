"""
Created on Sat Jan 22 19:17:00 2022

Dasturlash asoslari

16-dars NESTING
                    
@author: Sunnatillo Xayrullayev
"""

car0 = {
        'model':'lacetti','rang':'oq',
        'yil':2018, 'narx':13000,
        'km':5000, 'korobka':'avtomat'
        }
car1 = {
        'model':'nexia 3','rang':'qora',
        'yil':2015, 'narx':9000,
        'km':89000, 'korobka':'mexanika'
        }
car2 = {
        'model':'gentra','rang':'qizil',
        'yil':2019, 'narx':15000,
        'km':20000, 'korobka':'mexanika'
        }

car = car0
print(f"{car['model'].title()},\
 {car['rang']} rang,\
 {car['yil']}-yil, {car['narx']}$")
 
car = car1
print(f"{car['model'].title()},\
 {car['rang']} rang,\
 {car['yil']}-yil, {car['narx']}$")

car = car2
print(f"{car['model'].title()},\
 {car['rang']} rang,\
 {car['yil']}-yil, {car['narx']}$") 
 
# Yuqoridagi natijani chiqarishning osonroq usuli:

cars = [car0,car1,car2]  #lug'atlar ro'yxati
for car in cars:
    print(f"{car['model'].title()}, "
           f"{car['rang']} rang, "
           f"{car['yil']}-yil, {car['narx']}$")    
    
# Ro'yxat ichidagi istalgan lug'atga indeks bo'yicha murojaat qilish
print(cars[0]) 

# Biror lug'atdagi elementga murojaat qilish:
print(cars[0]['model'])
print(f"{cars[2]['rang'].title()} "
      f"{cars[2]['model']}")

# for sikli yordamida bo'sh lug'atlar yaratish
malibus = []  # Malibu mashinalari uchun bo'sh ro'yxat
for n in range(10):
    new_car = {   # har bir yangi avto uchun lug'at
        'model':'malibu',
        'rang':None,   # rangi noaniq
        'yil':2020,
        'narx':None,   # narxi belgilanmagan
        'km':0,
        'korobka':'avto'
        }
    malibus.append(new_car)  # lug'atni ro'yxatga qo'shamiz
    
# Yuqorida 10 ta malibudan iborat ro'yxat tuzdik va ularning ba'zilariga quyida qo'shimcha qiymat beramiz.
# Birinchi 3ta mashinaga qizil rang beramiz
for malibu in malibus[:3]:
    malibu['rang'] = 'qizil'
# keyingi 3 tasiga esa qora:
for malibu in malibus[3:6]:
    malibu['rang']='qora'
# Oxirgi 4 ta mashina rangi qora, korobkasi mexanika
for malibu in malibus[6:]:   # Oxirgi 4 ta mashinada
    malibu['rang']='qora'# rangi qora
    malibu['korobka']='mexanika'   # korobkasi mexanika
    
# Korobkasidan kelib chiqib narx belgilaymiz:
for malibu in malibus:
    if malibu['korobka']=='avto':
        malibu['narx']=40000
    else:
        malibu['narx']=35000
for malibu in malibus:
    print(malibu.values()) 

# LUG'AT ICHIDA RO'YXAT

dasturchilar = {
    'ali':['python','c++'],
    'vali':['html','css','js'],
    'hasan':['php','sql'],
    'husan':['python','php'],
    'maryam':['c++','c#']
    }
for ism, tillar in dasturchilar.items():
    print(f"\n{ism.title()}:", end='')
    for til in tillar:
        print(f'{til.upper()} ', end='')
        
# LUG'AT ICHIDA LUG'AT

hamkasblar = {
    'ali':{'familiya':'valiyev',
           't_yil':1995,
           'malumot':'oliy',
           'tillar':['python','c++']
           },
    'vali':{'familiya':'aliyev',
            't_yil':2001,
            'malumot':"o'rta maxsus",
            'tillar':['html','css','js']},
    'husan':{'familiya':'hasanov',
             't_yil':1999,
             'malumot':'maxsus',
             'tillar':['python','php']}
        }
for ism, info in hamkasblar.items():
    print(f"\n{ism.title()} {info['familiya'].title()}, "
          f"\n{info['t_yil']}-yilda tug'ilgan.\n"
          f"Ma'lumoti: {info['malumot']}. \n"
          "Quyidagi dasturlash tillarini biladi:")
    for til in info['tillar']:
        print(til.upper())
        
# AMALIYOT
# Adabiyot (ilm-fan, san'at, internet) olamidagi 4 ta mashxur shaxlar haqidagi ma'lumotlarni lug'at
# ko'rinishida saqlang. Lug'atlarni bitta ro'yxatga joylang, va har bir shaxs haqidagi ma'lumotni konsolga 
# chiqaring.

mshaxslar = {
    'alisher':{'familiya':'navoiy',
               'tyil':1441,
               'asarlari':'xamsa',
               'masarlari':'lison ut tayr',
               'tillar':['turkiy','forsiy','...']},
    'amir':{'familiya':'temur',
            'tyil':1336,
            'asarlari':'temur tuzuklari',
            'masarlari':'temur tuzuklari',
            'tillar':['turkiy','forsiy','arab','...']},
    'tohir':{'familiya':'malik',
             'tyil':1946,
             'asarlari':['shaytanat','alvido bolalik','...'],
             'masarlari':'Murdalar gapirmaydi',
             'tillar':["o'zbek",'rus','...']}
    }
for ism, info in mshaxslar.items():
    print(f"\n{ism.title()} {info['familiya'].title()}, "
          f"\n mashhur asarlari: {info['masarlari']}, "
          f"\n{info['tyil']}-yilda tug'ilgan. \n"
          f"Asarlari: {info['asarlari']},"
          f" Quyidagi tillarda gaplasha olgan:")
    for til in info['tillar']:    
       print(f"{til.upper()} ", end='' )
       
# Yuqoridagi lug'atlarga har bir shaxsning mashxur asarlari ro'yxatini ham qo'shing. For tsikli yordamida 
# muallifning ismi va uning asarlarini konsolga chiqaring.
       

mshaxslar = {
    'alisher':{'familiya':'navoiy',
              'asarlari':'xamsa',
               'masarlari':'lison ut tayr',
               'tillar':['turkiy','forsiy','...']},
    'amir':{'familiya':'temur',
            'tyil':1336,
            'asarlari':'',
            'masarlari':'temur tuzuklari',
            'tillar':['turkiy','forsiy','arab','...']},
    'tohir':{'familiya':'malik',
             'tyil':1946,
             'asarlari':['shaytanat','alvido bolalik','...'],
             'masarlari':'Murdalar gapirmaydi',
             'tillar':["o'zbek",'rus','...']}
    }
for ism, info in mshaxslar.items():
    print(f"\n{ism.title()} {info['familiya'].title() } ning mashhur asarlari:, "
          f"\n {info['masarlari']}, {info['asarlari']},")
    
# Oila a'zolaringiz (do'stlaringiz) dan 3 ta sevimli kino-seriali haqida so'rang. Do'stingiz ismi kalit,
# uning sevimli kinolarini esa ro'yxat ko'rinishida lug'artga saqlang.  Natijani konsolga chiqaring.
    
kinolar = {
    'olim':['bryus li','terminator','jumong'],
    'shuxrat':['kunfu','titanik','avatar'],
    'oybek':['transformer','vabank','jet li'] }
for ism, kinolar in kinolar.items():
    print(f"\n {ism.title()} ning sevimli kinolari:")
    for kino in kinolar:
        print(kino.title())
        
# Davlatlar degan lug'at yarating, lug'at ichida bir nechta davlatlar haqida ma'lumotlarni lug'at 
# ko'rinishida saqlang. Har bir davlat haqida ma'lumotni konsolga chiqaring.

davlatlar = {
    "o'zbekiston":{'poytaxt':'toshkent',
                  'hududi':448978,
                  'aholisi':35000000,
                  'pul birligi':'so\'m'},
    'koreya':{'poytaxt':'seul',
                  'hududi':219155,
                  'aholisi':77000000,
                  'pul birligi':'won'},
    'yaponiya':{'poytaxt':'tokio',
                  'hududi':377944,
                  'aholisi':125552000,
                  'pul birligi':'yen'}
    }
# for ism, info in davlatlar.items():
#     print(f"\n{ism.title()} ning poytaxti {info['poytaxt'].title()} shahri"
#           f"\n hududi: {info['hududi']} kv.km."
#           f"\n aholi soni: {info['aholisi']} kishi"
#           f"\n pul birligi: {info['pul birligi']}")
    
# Yuqoridagi dasturga o'zgartirish kiriting: konsolga barcha davlatlarni emas, foydalanuvchi so'ragan davlat
#  haqida ma'lumot bering. Agar davlat sizning lug'atingizda mavjud bo'lmasa, "Bizda bu davlat haqida
#  ma'lumot yo'q" degan xabarni chiqaring.
    
davlat = input('Davlat nomini kiriting: ').lower()
if davlat in davlatlar:
    info = davlatlar[davlat]
    print(f"\n{davlat.capitalize()} ning poytaxti {info['poytaxt'].title()} shahri"
          f"\n hududi: {info['hududi']} kv.km."
          f"\n aholi soni: {info['aholisi']} kishi"
          f"\n pul birligi: {info['pul birligi']}")
else:
    print("Bizda bu davlat haqida ma'lumot yo'q")    
        
