# 12-dars Xatolar bilan ishlash
"""
Created on Sun Jan 16 10:03:55 2022

Dasturlash asoslari

@author: Sunnatillo Xayrullaev
"""

# SintaxError
# print("hello world!"
#   # print'hello world!'
#           ^
# # SyntaxError: invalid syntax
# # parentheses - qavs

# print("hello world!"    
# SyntaxError: unexpected EOF while parsing. EOF-end of function

# print("hello world!    
      
# SyntaxError: EOL while scanning string literal. EOL-end of line

# IndentationError
#    print("hello world!")
# IndentationError: unexpected indent - kutilmagan bo'sh joy    

# TypeError

# son = input('Istalgan son kiriting: ')
# print(f'{son} ning kvadrati {son**2} ga teng')
# TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
# matn ya'ni string ustida arifmetik amallar bajarib bo'lmaydi. shuning uchun matnni avval int.ga o'zgartirish kerak
# son = input('Istalgan son kiriting: ')
# son = int(son)
# print(f'{son} ning kvadrati {son**2} ga teng')

# Name Error

# maxsulotlar = ['olma','uzum','anor','ananas','kivi','shaftoli','konfet']
# for maxsulot in mxsulotlar:
#     print(maxsulot)
# NameError: name 'mxsulotlar' is not defined

# Value Error

# son = int(input('Istalgan son kiriting: '))
# if son>=0:
#     print('Musbat son')
# else:
#     print('Manfiy son')
    
# ValueError: invalid literal for int() with base 10: '36.6'

# son = float(input('Istalgan son kiriting: '))
# if son>=0:
#     print('Musbat son')
# else:
#     print('Manfiy son')   
    
# Index Error

# mevalar = ['olma','uzum','anor']
# print(mevalar[3])
# IndexError: list index out of range

# # ZeroDivisionError
# x, y = 50, 50
# z = 250/(x-y)
# ZeroDivisionError: division by zero

# Mantiqiy xatolar

# radius = 5
# pi = 4.14
# aylana_yuzi = pi*radius**2
# print(f'S = {aylana_yuzi}')
# S = 103.49999999999999
# aslida S = 78.5 yuqorida pi qiymati noto'g'ri bo'lgani sababli javob noto'g'ri bo'ldi

# son = float(input('Istalgan son kiriting: '))
# ildiz = son**1/2
# print(f'{son} ning ildizi {ildiz} ga teng ')
# # Istalgan son kiriting: 9
# # 9.0 ning ildizi 4.5 ga teng 
# Yuqoridagi natijaga e'tibor bersangiz, 9 sonining ildizi 4.5 deb chiqdi. Sababi, 2-qatorda ildizni
# hisoblashda foydalanuvchi kiritgan son avval 1-darajaga oshirildi va undan keyin 2 ga bo'lindi. 
# Kodni to'g'rilaymiz:
# son = float(input("Istalgan son kiriting: "))
# ildiz = son**(1/2)
# print(f"{son} ning ildizi {ildiz} ga teng")

# Noo'rin bo'sh joy qoldirish (yoki qoldirmaslik) ham mantiqiy xatoga olib kelishi mumkin:
# mevalar = ['olma','uzum','nok','anor','anjir']
# for meva in mevalar:
#     print(meva)
#     print("Dastur tugadi")
# olma
# Dastur tugadi
# uzum
# Dastur tugadi
# nok
# Dastur tugadi
# anor
# Dastur tugadi
# anjir
# Dastur tugadi      
# Yuqorida "Dastur tugadi" matni bir marta, dastur tugaganidan so'ng chiqishi kerak edi. Lekin o'ngga surilib
# qolgani uchun bir necha bor qaytarildi. 

# mevalar = ['olma','uzum','nok','anor','anjir']
# for meva in mevalar:
#     print(meva)
# print("Dastur tugadi")
# Bundan boshqa ham mantiqiy xatoliklar juda ko'p uchraydi. 
# Mantiqiy xatoliklar mutlaqo topilmasdan ham qolib ketishi, va dastur bozorga chiqqanidan so'ng aniqlanishi 
# tabiiy hol. Shuning uchun ham aksar dasturlar tez-tez yangilanib turadi.  
# AMALIYOT
# Quyida Repl.it sahifasida bir nechta kodlar berilgan, kodlar avvalgi darsdagi uy vazifalaridan iborat. 
# Kodlardagi xatolarni toping va to'g'rilang. Har bir dasturda bir nechta xatolar mavjud bo'lishi mumkin. 
# Xatolarni topish uchun dasturlarni bir necha marta, turli qiymatlar bilan bajarib ko'ring. 
# Kodlarni kompyuterda tekshirish uchun quyidagi faylni yuklab oling:
    
# son = float(input("Juft son kiriting: "))
# if son%2 != 0:
#     print("Bu son juft emas")
# else:
#     print("Rahmat!")    

# yosh = int(input("Yoshingiz nechida?"))

# if yosh<=4 or yosh>=60:
#     narh = 0
# elif yosh < 18:
#     narh = 10000
# else:
#     narh = 20000
# print(f"Chipta {narh} so'm")

# x = float(input("Birinchi sonni kiriting: "))
# y = float(input("Ikkinchi sonni kiriting: "))
# if x==y:
#     print(f"{x}={y}")
# elif x<y:
#     print(f"{x}<{y}") 
# else:
#     print(f"{x}>{y}")

# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#                 'kartoshka', 'olma', 'banan', 'uzum', 'qovun']

# for n in range(5):
#     savat =[]
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))
#     if savat:
#       for mahsulot in savat:
#         if mahsulot in mahsulotlar:
#             print(f"Do'konimizda {mahsulot} bor")
#         else:
#             print(f"Do'konimizda {mahsulot} yo'q")
#     if savat == 0: 
#         print("Savatingiz bo'sh")            

# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#                 'kartoshka', 'olma', 'banan', 'uzum', 'qovun']


# savat = []
# for n in range(5):
#     savat.append(input(f'Savatga {n+1}-mahsulotni qo\'shing: '))

# bor_mahsulotlar = []
# mavjud_emas = []
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)

# if mavjud_emas:
#   print("Do'konimizda quyidagi mahsulotlar yo'q:")
#   for mahsulot in mavjud_emas:
#       print(mahsulot)
#   if mahsulot not in mavjud_emas:
#     print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
    
 
# users = ['alisher1983','aziza','yasina', 'umar']

# login = input("Yangi login tanlang:" )

# if login.lower() in users:
#       print('Login band, yangi login tanalng!')
# else:
#     print("Xush kelibsiz!")   