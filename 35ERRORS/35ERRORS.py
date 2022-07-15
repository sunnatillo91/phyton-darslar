# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 19:54:02 2022

#35-DARS. ERRORS

Author: Sunnatillo Xayrullayev
"""

# yosh = input("yoshingizni kiriting: ")
# yosh = int(yosh)
# print(f"Siz {2022-yosh} yilda tug'ilgansiz")

# yosh = input("Yoshingizni kiriting: ")
# try:
#     yosh = int(yosh)
   
# except:
#     print("Butun son kiritmadingiz")
    
# else:
#     print(f"Siz {2021-yosh} yilda tug'ilgansiz")
    
# print("dastur tugadi")

# MA'LUM TURDAGI XATOLARNI USHLASH

# yosh = input("Yoshingizni kiriting: ")
# try:
#     yosh = int(yosh)    
# except ValueError:
#     print("Butun son kiritmadingiz")
# else:
#     print(f"Siz {2021-yosh} yilda tug'ilgansiz")
    
#ZeroDivisionError
x,y=5,10
try:
   y/(x-5)
except ZeroDivisionError:
    print("0 ga bo'lib bo'lmaydi")
    
# IndexError

mevalar = ['olma','anor','anjir','uzum']
try:
    print(mevalar[7])
except IndexError:
    print(f"Ro'yxatda {len(mevalar)} ta meva bor xolos")
    
# KeyError

user = {"username":"sariqdev",
        "status":"admin",
        "email":"admin@sariq.dev",
        "phone":"99897123456"}

key="tel"
try:
    print(f'Foydalanuvchi: {user[key]}')
except KeyError:
    print("Bunday kalit mavjud emas")
    
# FileNotFoundError

# filename = "data.txt" # bunday fayl mavjud emas
# with open(filename) as f:
#     text = f.read()
# Natija: FileNotFoundError: [Errno 2] No such file or directory: 'data.txt'

filename = "data.txt" # bunday fayl mavjud emas
try:
    with open(filename) as f:
        text = f.read()
except FileNotFoundError:
    print(f"Kechirasiz, {filename} fayli mavjud emas. Boshqa fayl tanlang.")
    
# BIR NECHTA XATOLARNI USHLASH
# n = input("Butun son kiriting: ")
# try:
#     n = int(n)
#     x = 20/n
# except ValueError:
#     print("Butun son kiritmadingiz")
# except ZeroDivisionError:
#     print("0 ga bo'lish mumkin emas")
# else:
#     print(f"x = {x}")
    
# XATOLARNI KO'RSATMAY O'TISH
# import json 

# files = ['talaba1.json', 'talaba2.json', 'talab3.json', 'talaba4.json']
# for filename in files:
#     try:
#         with open(filename) as f:
#             talaba = json.load(f)
#     except FileNotFoundError:
#         print(f"{filename} mavjud emas")
        
#     else:
#         print(talaba['ism'])


import json 

files = ['talaba1.json', 'talaba2.json', 'talab3.json', 'talaba4.json']
for filename in files:
    try:
        with open(filename) as f:
            talaba = json.load(f)
    except FileNotFoundError:
        pass
        
    else:
        print(talaba['ism'])
        
        
# XATOLARNING OLDINI OLISH

while True:
    yosh = input("Yoshingizni kiriting: ")
    if yosh.isdigit():
        yosh = int(yosh)
        break
    
print(f"Siz {2022-yosh} yilda tug'ilgansiz")
    








