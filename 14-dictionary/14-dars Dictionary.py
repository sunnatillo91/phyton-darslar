"""
Created on Mon Jan 17 21:41:32 2022

Dasturlash asoslari

14-dars Dictionary (Lug'at)
                    
@author: Sunnatillo Xayrullaev
"""

# Lug'at bilan ishlash

car = {'model':'ferrari', 'rang':'qizil'}
# print(car['model'])
# print(car['rang'])

en_uz = {'apple':'olma','apricot':"O'rik",'banana':'banan'}
# print(en_uz['apple'])

talaba = {'ism':'murod olimov','yosh':20, 't_yil':2000}
# print(f"{talaba['ism'].title()}, \
#  {talaba['t_yil']}-yilda tug'ilgan, \
#  {talaba['yosh']} yoshda")    

car = {
       'make':'GM',
       'model':'Malibu',
       'colour':'Black',
       'gear':'Automatic',
       'year':'2022',
       'price':40000
       }

# get() metodi

# print(car['model'])       
# print(car['narx'])
# Lug'atda 'narx' kalit so'zi bo'lmagani uchun, KeyError: 'narx' degan xatoni qaytardi.      
narx = car.get('narx', 'Bunday kalit mavjud emas')
print(narx)

narx = car.get('narx')
print(narx)

# Yangi juftlik qo'shish

talaba['kurs'] = 4
talaba['fakultet'] = 'konchilik' 
print(talaba)

#Bo'sh lug'at

car = {}
car['model'] = 'Mazda 6'
car['colour'] = 'Red'
car['price'] = 40000
print(f"{car['colour']} {car['model']}, {car['price']}$")
# result: Red Mazda 6, 40000$

# Qiymatni o'zgartirish

car['price']=38000
print(f"{car['colour']} {car['model']}, {car['price']}$")

# Kalit so'z-qiymat juftligini o'chirish

car = {'model':'Malibu','colour':'Black', 'price':40000}
print(car)
del car['colour']
print(car)

# Lug'atlarni bir nechta qatorda yozish

telefonlar = {
    'ali':'iphone x',
    'vali':'samsung s9',
    'olim':'mi 10 pro',
    'orif':'samsung a10'
    }
print(telefonlar)

# Amaliyot

# otam (onam, akam, ukam, va hokazo) degan lug'at yarating va lug'atga shu inson haqida kamida 3 ta
# m'alumot kiriting (ismi, tu'gilgan yili, shahri, manzili va hokazo). Lug'atdagi ma'lumotni matn shaklida 
# konsolga chiqaring :Otamning ismi Mavlutdin, 1954-yilda, Samarqand viloyatida tug'ilgan
otam = {'yosh':56, 'yashash joyi':'Samarqand','hobbiy':'Bog\'dorchilik'}
onam = {'yosh':53, 'yashash joyi':'Samarqand','hobbiy':'jevellery'}
print(f"otamning yoshi {otam['yosh']} da, {otam['yashash joyi']}da tug\'ilgan.")
print(f"onamning yoshi {onam['yosh']} da, {onam['yashash joyi']}da tug\'ilgan")

# Oila a'zolaringizning sevimli taomlari lug'atini tuzing. Lug'atda kamida 5 ta ism-taom jufltigi bo'lsin.
# Kamida uch kishining sevimli taomini konsolga chiqaring: Alining sevimli taomi osh

sevimli_taomlar = {'Umar':'osh', 'Abdulloh':'baliq', 'Ali':'xonim'}
print(sevimli_taomlar)
print(f"Abdullohning sevimli taomi: {sevimli_taomlar['Abdulloh']}")
print(f"Alining sevimli taomi: {sevimli_taomlar['Ali']}")
print(f"Umarning sevimli taomi: {sevimli_taomlar['Umar']}")

# Python izohli lu'gati tuzing: Lug'atga shu kunga qadar o'rgangan 10 ta so'z (atamani) kiriting (masalan 
# integer, float, string, if, else va hokazo) va har birining qisqacha tarjimasini yozing.

dictionary = {'integer':'butun son',
              'float':'o\'nlik son',
              'string':'matn',
              'if':'agar',
              'lists':'ro\'yxatlar',
              'tuples':'o\'zgarmas ro\'yxatlar',
              'print':'natijani konsolga chiqarish',
              "input()":'foydalanuvchi bilan muloqot',
              'variables':'o\'zgaruvchilar',
              '.append()':'ro\'yxatga ma\'lumot qo\'shish'
              }

# Foydalanuvchidan biror so'z kiritishni so'rang va so'zning tarjimasini yuqoridagi lug'atdan 
# chiqarib bering.
# Agar so'z lu'gatda mavjud bo'lmasa, "Bunda so'z mavjud emas" degan xabarni chiqaring. 

kalit = input('kalit so\'z kiriting: \n').lower()    
# print(dictionary.get(kalit, 'Bunday so\'z mavjud emas'))

# Yuqoridagi vazifani if-else yordamida qiling va natijani ham foydalanuvchiga tushunarli 
# ko'rinishda chiqaring.

kalit = input('kalit so\'z kiriting: \n').lower()    
tarjima = dictionary.get(kalit)
if tarjima == None:
   print("Bunday so'z mavjud emas")
else:
   print(f"{kalit.title} so'zi, {tarjima} deb tarjima qilinadi") 
   
    