#11-dars Shartlar if-elif-else
"""
Created on Fri Jan 14 09:24:28 2022

Dasturlash asoslari

@author: Sunnatillo Xayrullaev
"""
# elif - else va if so'zalrining jamlanmasi bo'lib, "aks holda, agar" deb tarjima qilinadi. 
# Bunday if bilan boshlangan ketma-ketlik bir nechta elif lardan iborat bo'lishi mumkin. 

# son = int(input("Son kiriting: "))
# if son>0:
#     print("Son musbat")
# elif son<0:
#     print("Son manfiy")
# else:
#     print('Son 0 ga teng')    
    
#Diqqat! if-elif-else ketma-ketlikda biror shart bajarilishi bilan, Python qolgan 
#shartlarni tekshirmaydi.    

# yosh = int(input("Yoshingiz nechida? "))
# if yosh<4:
#     print("Sizga kirish bepul")
# elif yosh<=12:
#     print("Sizga kirish 5000 so'm")
# else:
#     narx = 10000    
#     print("Sizga kirish 10000 so'm")    

# yosh = int(input("Yoshingiz nechida? "))
# if yosh<4:
#     narx= "bepul"
# elif yosh<=12:
#     narx = 5000 
# else:
#     narx = 10000    
# print(f"Sizga kirish {narx} so'm")   

# yosh = int(input("Yoshingiz nechida? "))
# if yosh<4:
#     narx= "bepul"
# elif yosh<=12:
#     narx = 5000 
# elif yosh<=18:
#     narx = 8000    
# else:
#     narx = 10000    
# print(f"Sizga kirish {narx} so'm")   

# if-elif-else zanjirda else qismi majburiy emas
# yosh = int(input("Yoshingiz nechida? "))
# if yosh<4:
#     narx= "bepul"
# elif yosh<=12:
#     narx = 5000 
# elif yosh<=18:
#     narx = 8000    
# elif yosh>18:
#     narx = 10000    
# print(f"Sizga kirish {narx} so'm")   

# AND va OR operatorlari
# kun = input("bugun qaysi kun? ")
# if kun.lower()=='shanba' or kun.lower()=='yakshanba':
#     print('Bugun dam olish kuni.')
# else:
#    print('Bugun ish kuni.')     
   
# kun = input("Bugun qaysi kun? ")
# # harorat = float(input("Havo harorati qanday? "))
# # if kun.lower()=='yakshanba' and harorat>=30:
# #     print("Cho'milgani ketdik!")
# # elif kun.lower()=='yakshanba' and harorat<30:
# #     print("Uyda dam olamiz!")

# yosh = int(input("Yoshingizni kiriting\n"))
# if (yosh<7 or yosh>65) and kun=='chorshanba':
#     print('Bugun siz uchun Muzeyga kirish bepul')
    
# # Boolean ma'lumotlar turi
# a=True
# b=False

# narx = 15000  # mijoz 150000 so'mga taom oldi
# choy = True  #mijoz choy ham oldi
# salat = False  #mijoz salat olmadi
# if choy and salat:  #agar mijoz choy va salat olgan bo'lsa,
#     narx = narx+10000   #narxga 10000 so'm qo'shamiz
# elif choy or salat:  #agar choy yoki salat olgan bo'lsa,
#    narx=narx+5000   #narxga 5000 so'm qo'shamiz
   
# print(f"Jami {narx} so'm")  #yakuniy narxni chiqaramiz   


# #Shartlarni ketma-ket tekshirish
# narx = 15000  # mijoz 150000 so'mga taom oldi
# choy = True  #mijoz choy ham oldi
# salat = False  #mijoz salat olmadi
# non= True
# kompot = True
# assorti = False
# if choy:  #agar mijoz choy olgan bo'lsa,
#     print("Mijoz choy oldi.")
#     narx = narx+3000   #narxga 3000 so'm qo'shamiz
# if salat:  #agar mijoz salat olgan bo'lsa,
#     print("Mijoz salat oldi.")
#     narx = narx+5000   #narxga 5000 so'm qo'shamiz    
# if non:  #agar mijoz non olgan bo'lsa,
#     print("Mijoz non oldi.")
#     narx = narx+2000   #narxga 5000 so'm qo'shamiz      
# if kompot:  #agar mijoz kompot olgan bo'lsa,
#     print("Mijoz kompot oldi.")
#     narx = narx+5000   #narxga 5000 so'm qo'shamiz  
# if assorti:  #agar mijoz assorti olgan bo'lsa,
#     print("Mijoz assorti oldi.")
#     narx = narx+15000   #narxga 5000 so'm qo'shamiz      
   
# print(f"Jami {narx} so'm")  #yakuniy narxni chiqaramiz   
   
# # Ro'yxat tarkibini tekshirish
# menyu = ['osh','qozonkabob','shashlik','norin','somsa']
# 'manti'in menyu  #menyuda manti bormi?

# menyu = ['osh','qozonkabob','shashlik','norin','somsa']
# ovqat = input('Nima ovqat yeysiz?\n')
# if ovqat.lower() in menyu:
#     print('Buyurtma qabul qilindi.')
# else:
#     print('Afsuski, bizda bunday ovqat yo\'q.')    
    
# menyu = ['osh','qozonkabob','shashlik','norin','somsa']
# ovqat = input('Nima ovqat yeysiz?\n')
# if ovqat.lower() not in menyu:
#     print('Afsuski, bizda bunday ovqat yo\'q.')  
# else:
#     print('Buyurtma qabul qilindi.')

# Ikki ro'yxatni solishtirish    
# menyu = ['osh','qozonkabob','shashlik','norin','somsa']
# buyurtmalar = ['osh','somsa','manti','shashlik']
# if buyurtmalar:  #ro'yxatda biror element bo'lsa ifoda True qaytaradi
#   for taom in buyurtmalar:
#     if taom in menyu:
#         print(f'Menyuda {taom} bor')
#     else:
#         print(f'Kechirasiz, menyuda {taom} yo\'q.')
# else:
#    print('Savatchangiz bo\'sh')        
        
# Amaliyot

# Quyidagi dasturlarni alohida fayllarga yozing va bajaring:
# Foydalanuvchidan juft son kiritishni so'rang. Agar foydalanuvchi juft son kiritsa "Rahmat!",
# agar toq son kiritsa "Bu son juft emas" degan xabarni chiqaring.   
# son = int(input('Juft son kiriting:\n'))
# if son%2 == 0:
#     print('Rahmat!')
# else:
#    print('Bu son juft emas')    
   
# Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini quyidagicha chiqaring:
# Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo'lsa bepul
# Agar foydalanuvchi 18 dan kichik bo'lsa 10000 so'm
# Agar foydalanuvchi 18 dan katta bo'lsa 20000 so'm
# yosh = int(input('Yoshingiz nechida?\n'))
# if yosh<4 or yosh>60:
#     narx = 0
# elif yosh<18:
#     narx=10000
# elif yosh>=18:
#    narx = 20000
# print(f'Sizga muzeyga kirish {narx} so\'m.')    

# Foydalanuvchidan ikita son kiritishni so'rang, sonlarni solishtiring va ularning teng
# # yoki katta/kichikligi haqida xabarni chiqaring   
# a = int(input("Birinchi sonni kiriting:\n"))
# b = int(input("Ikkinchi sonni kiriting:\n"))
# if a > b:
#     print(f'{a} > {b} ')
# elif a<b:
#     print(f'{a}<{b}')    
# else:
#   print(a=b)    

# mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting. Yangi, 
# savat degan bo'sh ro'yxat yarating va foydalanuvchidan savatga kamida 5 ta mahsulot 
# kiritishni so'rang. Savatdagi elementlarni, mahsulotlar ro'yxati bilan solishtiring va qaysi
# biri ro'yxatda bo'lsa "Mahsulot do'konimizda bor" aks holda, "Mahsulot do'konimizda yo'q"
# degan xabarlarni chiqaring.

# maxsulotlar = ['olma','uzum','anor','ananas','kivi','shaftoli','konfet','go\'sht','non','tuxum']
# savat = []
# savat.append(input('1-buyurtma:'))
# savat.append(input('2-buyurtma:'))
# savat.append(input('3-buyurtma:'))
# savat.append(input('4-buyurtma:'))
# savat.append(input('5-buyurtma:'))
# if savat:
#     for buyurtma in savat:
#         if buyurtma in maxsulotlar:
#           print(f"do'konimizda {buyurtma} bor")
#         else:
#           print(f"do'konimizda {buyurtma} yo'q")
          
# Yuqoridagi dasturni quyidagicha o'zgartiring: foydalanuvchidan 5 ta mahsulot kiritishni 
# so'rang. Foydalanuvchi so'ragan va do'konda bor mahsulotlarni yang, bor_mahsulotlar degan 
# ro'yxatga, do'konda yo'q mahsulotlarni esa mavjud_emas degan ro'yxatga qo'shing.  
# Agar mavjud_emas ro'yxati bo'sh bo'lsa, "Siz so'ragan barcha mahsulotlar do'konimizda bor"
# degan xabarni, aks holda esa "Quyidagi mahsulotlar do'konimizda yo'q.." degan xabarni chiqaring.

maxsulotlar = ['olma','uzum','anor','ananas','kivi','shaftoli','konfet','go\'sht','non','tuxum']
savat = []
for n in range(5):
    savat.append(input(f"{n+1}-buyurtma: "))
# savat.append(input('1-buyurtma:'))
# savat.append(input('2-buyurtma:'))
# savat.append(input('3-buyurtma:'))
# savat.append(input('4-buyurtma:'))
# savat.append(input('5-buyurtma:'))
# if savat:          
#     for buyurtma in savat:
#         if buyurtma in maxsulotlar:
#             bor_maxsulotlar = []
#             bor_maxsulotlar.append(buyurtma)
#             #print(bor_maxsulotlar)
#         if buyurtma not in maxsulotlar:
#               mavjud_emas = []
#               mavjud_emas.append(buyurtma)
#               print(f"Quyidagi maxsulotlar do'konimizda yo'q: {mavjud_emas}")
#         else:
#            print('Siz so\'ragan barcha maxsulotlar do\'konimizda bor')
          
# # if mavjud_emas:
# #   print("Do'konimizda quyidagi mahsulotlar yo'q:")
# #   for mahsulot in mavjud_emas:
# #     print(mahsulot)
# else:
#   print("Siz so'ragan barcha mahsulotlar do'konimizda bor")          
# foydalanuvchilar degan ro'yxat tuzing, va kamida 5 ta login qo'shing. Foydalanuvchidan yangi login tanlashni
# so'rang va foydalanuvchi kiritgan loginni foydalanuvchilar degan ro'yxatning tarkibi bilan solishtiring.
# Agar ro'yxatda bunday login mavjud bo'lsa, "Login band, yangi login tanlang!" aks holda "Xush kelibsiz,
# foydalanuvchi!" xabarini chiqaring
          
foydalanuvchilar = ['sunnat','olim','kamol','sharif','zarif']
login = input('Login kiriting:')

if login in foydalanuvchilar:    
    print("Login band, yangi login tanlang!")
else:
    print(f"Xush kelibsiz, {login}!")           
  
# foydalanuvchilar = ['sunnat','olim','kamol',  
# Foydalanuvchidan biror butun son kiritishni so'rang. Foydalanuvchi kiritgan sonni 2 dan 10 gacha bo'lgan 
# sonlardan qay biriga qoldiqsiz bo'linishini konsolga chiqaring. 

# son = int(input("Istalgan butun son kiriting: "))
# for n in range(2,11):
#    if not son%n:
#        print(f"{son} soni {n} ga qoldiqsiz bo'linadi")

# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#                'kartoshka', 'olma', 'banan', 'uzum', 'qovun']


# savat = []
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

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
#     print(mahsulot)
# else:
#   print("Siz so'ragan barcha mahsulotlar do'konimizda bor")