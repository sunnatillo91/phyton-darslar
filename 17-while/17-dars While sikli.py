"""
Created on Sun Jan 23 08:25:15 2022

Dasturlash asoslari

17-dars while SIKLI
                    
@author: Sunnatillo Xayrullayev
"""

# # while QANDAY ISHLAYDI?
# son = 1
# while son<= 5:  # toki son 5 dan kichik yoki teng ekan...
#     print(son, end=' ')    # sonni konsolga chiqaramiz va
#     son  = son+1   # songa 1ni qo'shamiz  son  += 1
    
# while va input()
# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol+= "(to'xtatish uchun 'exit' deb yozing): "
# qiymat = ''
# while qiymat !='exit':   # toki qiymat exitga teng emas ekan
#     qiymat = input(savol)    
#     if qiymat != 'exit':
        # print(float(qiymat)**2)
        
# ISHORA-FLAG

# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol+= "(to'xtatish uchun 'exit' deb yozing): "
# ishora = True
# while ishora:    # toki ishora=True ekan
#     qiymat = input(savol)    
#     if qiymat == 'exit':
#         ishora = False
#     else:    
#         print(float(qiymat)**2)
# print("Dastur tugadi")   

# break OPERATORI
 
# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol+= "(to'xtatish uchun 'exit' deb yozing): "
# while True:    # toki ishora=True ekan
#     qiymat = input(savol)    
#     if qiymat == 'exit':
#         break   # siklni to'xtatish
#     else:    
#         print(float(qiymat)**2)
# print("Dastur tugadi")        

# break operatori for siklini to'xtatish uchun ham ishlatiladi

# sonlar = list(range(1,11))
# for son in sonlar:
#     if son == 5:   # son 5 ga teng bo'lsa
#       break     # sikl to'xtaydi
#     print(f"{son} ning kvadrati {son**2} ga teng")  

# continue operatori
# bu operator ma'lum bir shart bajarilganda qadam tashlash uchun mo'ljallangan


# sonlar = list(range(1,11))
# for son in sonlar:
#     if son == 5:   # son 5 ga teng bo'lsa
#       continue     
#     print(f"{son} ning kvadrati {son**2} ga teng")  

# son = 0
# while son < 10:
#     son+=1
#     if son%2 !=0:   # agar son toq bo'lsa
#         continue
#     else:  #aks holda (juft bo'lsa)
#         print(son, end=' ')
        
#  Sikl ichida bir nechta continue operatori bo'lishi mumkin

# ABADIY SIKL TUZOG'I

# Tsikllar bilan ishlashda abadiy tsikl yaratib qo'yishdan ehtiyot bo'lishimiz kerak. Abadiy tsiklga turli 
# mantiqiy xatolar sabab bo'lishi mumkin: noto'g'ri shart, o'zgarmas qiymat, kodlar ketma-ketligida xatolik va
#  hokazo. 

# Dastur bajarilishini to'xtatish uchun konsolda Ctrl+C tugmasini bosing

# son = 0
# while son<10:
#     if son%2!=0:
#         continue
#     else:
#         print(son)
# Yuqoridagi kod abadiy davom etadi, sababi biz sonning qiymatini o'zgartirishni esdan chiqardik
                         
# son = 0
# while son<10:
#     if son%2 !=0:
#         continue
#     else:
#         print(son)
#     son +=1         
    # Yuqoridagi kod abadiy davom etadi
    
# son = 1
# while son>0:
#     son+=1
#     if son%2!=0:
#         continue
#     else:
#         print(son)
        
# Yuqoridagi kodda xato shart tufayli (son>0) sikl abadiy davom etadi        

# Foydalanuvchidan yaxshi ko'rgan kitoblarini kiritishni so'rang. Foydalanuvchi stop so'zini yozishi bilan
#  dasturni to'xtating
# savol = "Yaxshi ko'rgan kitoblaringiz nomini kiriting"
# savol+= "(to'xtash uchun 'stop' deb yozing): "
# qiymat = ''
# while qiymat != 'stop':
#     qiymat = input(savol)
#     if qiymat != 'stop':
#         print(qiymat.title())
 

# Muzeyga chipta narhi foydalanuvchining yoshiga bog'liq: 7 dan yoshlarga - 2000 so'm, 7-18 gacha 3000 so'm,
#  18-65 gacha 10000 so'm, 65 dan kattalarga bepul. Shunday while tsikl yozingki, dastur foydalanuvchi
#  yoshini so'rasin va chipta narhini chiqarsin. Foydalanuvchi exit yoki quit deb yozganda dastur to'xtasin
#  (ikkita shartni ham tekshiring).

# savol = "Yoshingiz nechida?: "
# savol+="(to'xtash uchun 'exit' yoki 'quit' deb yozing): "

# while True !='exit' or 'quit':
#     qiymat = input(savol)
#     if qiymat == 'exit' or qiymat == 'quit':
#         break
#     yosh = int(qiymat)
    
#     if yosh < 7:
#         narx = 2000
#     elif 7<=yosh<18:
#         narx = 3000
#     elif 18<=yosh<65:
#         narx = 10000
#     else:
#         narx = 0
        
#     if narx == 0:
#         print("Sizga chipta bepul")
#     else:
#         print(f"Sizga chipta narxi {narx} so'm")

# Yuqoridagi dasturni turli usullarda yozib ko'ring (break, ishora, yoki shart tekshirish)

# savol = "Yoshingiz nechida?: "
# savol+="(to'xtash uchun 'exit' yoki 'quit' deb yozing): "
# ishora = True
# while ishora !='exit' or 'quit':
#     qiymat = input(savol)
#     if qiymat == 'exit' or qiymat == 'quit':
#         ishora = False
#     yosh = int(qiymat)
    
#     if yosh < 7:
#         narx = 2000
#     elif 7<=yosh<18:
#         narx = 3000
#     elif 18<=yosh<65:
#         narx = 10000
#     else:
#         narx = 0
        
#     if narx == 0:
#         print("Sizga chipta bepul")
#     else:
#         print(f"Sizga chipta narxi {narx} so'm")

# Quyidagi dasturda bir nechta mantiqiy xatolar bor. Jumladan, xusisiy holatlarda tsikl abadiy qaytarilib 
# qolmoqda. Xatolarni to'g'rilay olasizmi?

savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True !='exit':
    qiymat = input(savol)
    if qiymat =='exit':
        break
    elif float(qiymat)<0:
        continue
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")
