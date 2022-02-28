#10-dars Shartlar
"""
Created on Thu Jan 13 20:56:14 2022

Dasturlash asoslari

@author: Sunnatillo Xayrullaev
"""
# Taqqoslash operatori
# tenglik          ==
# tengsizlik       !=
# Kichik           <
# kichik yoki teng <=
# katta            >
# katta yoki teng  >=

# avtolar = ['bmw','audi','gm','lamborgini', 'tesla']
# for avto in avtolar:
#     if avto=='bmw':  # agar avto bmw ga teng bo'lsa'
#        print(avto.upper()) # avtoni hamma harflarini katta harfda yoz  
#     else:
#         print(avto.title())
# ism=input('Ismingiz nima?\n')
# if ism.lower() != 'ali':
#     print(f'Uzr,{ism.lower()}, biz Alini kutayapmiz.')  
# else:
#     print('Salom, Ali')
    
# a=5
# b=6
# print(a==b)    

# a=5
# b=6
# print(a==(b-1))    

# print('Anvar'=='anvar') # mtnlarni taqqoslash

# print(10**2<2**10)  # sonlarni taqqoslash

# ism='ahad'
# # print(ism!='Ahad')
                
# print(ism.title()=='Ahad')

# nums1=[1,2,3]
# nums2=[1,2,4]
# print(nums1!=nums2)
# print(9**2>=7*9+18)

# x=10
# print(x*x<2**2)

#if-else operatori

# son=int(input('Istalgan son kiriting: '))
# if son>0:
#     print(son, 'musbat son')

# yosh=int(input("Yoshingizni kiriting: "))
# if yosh<=7:  # agar yosh7 dan kichik yoki teng bo'lsa
#    print('Sizga avtobus bepul')
# else:
#     print("Chipta narxi 5 000 so'm")
    
# yosh=int(input("Yoshingiz nechchida?  "))
# if yosh>65: print("Siz COVID-19 risk guruhida ekansiz")

# avtolar=["bmw","toyota","mersides","kia"]
# for avto in avtolar:
#     if avto=='bmw':
#       print(avto.upper())
#     else:
#         print(avto.title())
        
# javob= float(input('12*6 nechiga teng? ')) 
# if javob !=72:
#    print("Javob xato!")       

# yosh = int(input("Yoshingiz nechida? "))
# if yosh>=18:
#     print("Xush kelibsiz! ")
# else:
#     print("Kirish mumkin emas!")    
   
# yil = int(input("Tug'ilgan yilingizni kiriting:"))
# if 2021-yil<18:
#     print(f'Yoshingiz {2021-yil} da ekan.')
#     print("Kirish mumkin emas!")
# else:
#     print("Xush kelibsiz!")    
    
# login = input("Yangi logi tanlang:")
# if len(login)<=5: # login uzunligini tekshiramiz
#    print("Login 5 harfdan ko'proq bo'lishi shart!")
   
# Yangi cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] degan ro'yxat tuzing, ro'yxat 
# elementlarining birinchi harfini katta qilib konsolga chqaring. GM uchun ikkala harfni katta qiling
    
# Yangi_cars = ['toyota', 'mazda','hyundai','gm','kia']
# for car in Yangi_cars:
#     if car == 'gm':
#         print(car.upper())
#     else:
#         print(car.title())

# # Yuqoridagi mashqni teng emas (!=) operatori yordamida bajaring. 
# Yangi_cars = ['toyota', 'mazda','hyundai','gm','kia']
# for car in Yangi_cars:
#     if car != 'gm':
#        print(car.title())
#     else:
#         print(car.upper())
        
# Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa, "Xush kelibsiz, Admin. 
# Foydalanuvchilar ro'yxatini ko'rasizmi?" xabarini konsolga chiqaring. Aks holda, 
# "Xush kelibsiz, {foydalanuvchi_ismi}!"  matnini konsolga chiqaring.
# login = input(f"Loginni kiriting:")
# if login == "admin":
#     print("Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?")
# else:
#     print("Xush kelibsiz, {login} ")

# Foydalanuvchidan 2 ta son kiritishni so'rang. Agar ikki son bir-biriga teng bo'lsa,
# "Sonlar teng" ekan degan yozuvni konsolga chiqaring.

# x = float(input("1- sonni kiriting:"))
# y = float(input("2- sonni kiriting:"))
# if x == y: print(f"Sonlar teng: {x}={y}")
        
# Foydalanuvchidan istalgan son kiritishni so'rang. Agar son manfiy bo'lsa konsolga
# "Manfiy son", agar musbat bo'lsa "Musbat son" degan xabarni chiqaring. 
# son = float(input("Istalgan son kiriting: "))
# if son < 0:
#     print("Manfiy son")
# else:
#     print("Musbat son")    

# Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa uning ildizini hisoblab 
# konsolga chiqaring. Agar son manfiy bo'lsa, "Musbat son kiriting" degan xabarni chiqaring.
        
# son = float(input("Istalgan son kiriting:\n"))
# if son > 0: print(son**(0.5))
# # else: print("Musbat son kiriting")

# a = int(input("Istalgan son kiriting:"))
# if a%2==0:
#     print("Juft son")
# else:
#     print("Toq son")    
 
 

