"""
Created on Wed Jan 26 21:51:24 2022

Dasturlash asoslari

19-dars xatolar bilan ishlash
                    
@author: Sunnatillo Xayrullayev
"""

# EXCEPTIONS
# try-except

# yosh = input("Yoshingizni kiriting: ")
# yosh = int(yosh)   
# print(f"Siz {2022-yosh} yilda tug'ilgansiz") 
 
# ValueError: invalid literal for int() with base 10: '30.5'
# Yuqoridagi xatoni oldini olish uchun xato yuz berishi mumkin bo'lgan qatorlarni try-except bloki yordamida yozamiz

# yosh = input("Yoshingizni kiriting: ")
# try:
#     yosh = int(yosh)   # xato qaytargan qator
# except:
#     print("Butun son kiritmadingiz")
# else:
#     print(f"Siz {2022-yosh} yilda tug'ilgansiz") 

# Ma'lum turdagi xatolar bilan ishlash


# yosh = input("Yoshingizni kiriting: ")
# try:
#     yosh = int(yosh)
# except ValueError:
#     print("Butun son kiritmadingiz")
# else:
#     print(f"Siz {2022-yosh} yilda tug'ilgansiz") 

# ZeroDivisionError
# x,y = 5,10
# try:
#     y/(x-5)
# except ZeroDivisionError:
#     print("0 ga bo'lish mumkin emas")
    
# # Indexerror

# mevalar = ['olma','anor','anjir','uzum']
# try:
#     print(mevalar[7])
# except IndexError:
#     print(f"Ro'yxatda {len(mevalar)} ta meva bor xolos")
    
# # KeyError

# user = {"username":"sariqdev",
#         "status":"admin",
#         "email":"admin@sariqdev",
#         "phone":"99897123456"}
# key = 'tel'
# try:
#     print(f'Foydalanuvchi: {user[key]}')   
# except KeyError:
#     print("Bunday kalit mavjud emas")

# # FileNotFoundError

# fayl = "data.txt"  #bunday fayl mavjud emas
# try:  # faylni ochishga harakat qilamiz
#     f=open(fayl)
# except FileNotFoundError:
#     print(f"{fayl} fayli mavjud emas.")   
     
# # BIR NECHA XATOLARNI USHLASH

# n = input("Butun son kiriting: ")
# try:
#     n=int(n)
#     x=20/n
# except ValueError:  # Agar foydalanuvchi butun son kiritmasa
#     print("Butun son kiritmadingiz")
# except ZeroDivisionError:  # agar foydalanuvchi 0 kiritsa,
#     print("0 ga bo'lish mumkinmas")
# else:
#     print(f"x={x}")    
    
# # Xatolarni ko'rsatmay o'tish

# user = {"username":"sariqdev",
#         "status":"admin",
#         "email":"admin@sariq.dev",
#         "phone":"998997123456"}    
# key = "tel"
# try:
#     print(f'Foydalanuvchi: {user[key]}') 
# except KeyError:
#     pass
    
# if yosh<20:
#     pass
# else:
#     pass

# # Xatolarning oldini olish

# yosh = input("Yoshingizni kiriting: ")
# try:
#     yosh = int(yosh)  # Xato qaytargan qator
#     print(f"Siz {2022-yosh} yilda tug'ilgansiz")
# except:  # xatoyuz bergan bajariluvchi kod
#     print("Butun son kiritmadingiz")

# while True:
#     yosh = input("Yoshingizni kiriting: ")
#     if yosh.isdigit():
#         yosh = int(yosh)
#         break
# print(f"Siz {2022-yosh} yilda tug'ilgansiz")    

# AMALIYOT
# Quyidagi kod bajarilishida yuzaga kelishi mumkin bo'lgan xatolarni ushlab,xatoga mos matnni konsolga chiqaring
# x= input("son kiriting: ")
# try:
#     x = int(x)
#     print(f"x = {x}")
# except:
#     print("Butun son kiritmadingiz")    
# x= input("Yana bir son kiriting: ")
# try:
#     x = int(x)
#     print(f"x = {x}")
# except:
#     print("Butun son kiritmadingiz")    
    
# Yuqoridagi kodni while sikli yordamida xato qiymat kiritilganda takrorlanadigan qiling.

while True:
    x= input("son kiriting: ")
    if x.isdigit():
        x = int(x)
        break
print(f"x ning qiymati {x}")    

while True:
    x= input("Yana bir son kiriting: ")
    if x.isdigit():
        x = int(x)
        break
print(f"x ning qiymati {x} ga teng")    