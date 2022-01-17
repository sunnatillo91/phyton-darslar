# 09-dars for Sikli
"""
Created on Wed Jan 12 19:41:25 2022

Dasturlash asoslari

@author: S.Khayrullaev
"""

# mehmonlar=['Ali','Vali','Hasan','Husan','Olim']
# for mehmon in mehmonlar:
#     print(mehmon)

# mehmonlar=['Ali','Vali','Hasan','Husan','Olim']
# for mehmon in mehmonlar:   # Sikl sharti
#     print('Hurmatli', mehmon)    # Sikl badanidagi kod
#     print('Sizni 20-mart kungi nahorgi oshga taklif qilamiz.')
#     print('Hurmat bilan, palonchiyevlar oilasi')
    
#Tsikl badani surilish (indentation) bilan ajratiladi, ya'ni tsiklning takrorlanuvchi qismi 
#asosiy koddan bir muncha o'ngroqqa surilgan bo'ladi. Agar biz mana shu surilishni tark 
#qilsak kodimiz xato beradi:   
 
# mehmonlar = ['Ali','Vali','Hasan', 'Husan','Olim']
# for mehmon in mehmonlar:
# print(f"Hurmatli {mehmon}, sizni 20 Dekabr kuni nahorga oshga taklif qilamiz")
# print("Hurmat bilan, Palonchiyevlar oilasi\n")
# Natija: IndentationError: expected an indented block

# Shunigdek, ko'pchilik yo'l qo'yadigan yana bir xato, qo'shimcha qatorlarni surish esdan chiqishi:
# mehmonlar = ['Ali','Vali','Hasan', 'Husan','Olim']
# for mehmon in mehmonlar:
#     print(f"Hurmatli {mehmon}, sizni 20 Dekabr kuni nahorga oshga taklif qilamiz")
# print("Hurmat bilan, Palonchiyevlar oilasi\n")
    
# cars=['nexia','tico','damas']   
# for car in cars:  #  <- sikl sharti
#     print(car.title())  # <-sikl badani
# print("Ko'rganlar qilar havas!")    

# cars=['nexia','tico','damas']   
# for car in cars:  #  <- sikl sharti
#     print(car.title())  # <-sikl badani
    
#     print("Ko'rganlar qilar havas!")   

# for yordamida sonli ro'yxatlar bilan ishlash
# sonlar=list(range(1,11))    
# for son in sonlar:
#     print(f'{son} ning kvadrati {son**2} ga teng')
    
# sonlar=list(range(11))  #1 dan 10 gacha sonlar ro'yxati
# sonlar_kvadrati=[]  # bo'sh ro'yxat
# for son in sonlar:
#     sonlar_kvadrati.append(son**2)
# print(sonlar)
# print(sonlar_kvadrati)    

# # for va input()
# dostlar=[]  #bo'sh ro'yxat
# print("5 ta eng eng yaqin do'stingiz kim?")
# for n in range(5):
#    dostlar.append(input(f"{n+1}-do'stingizning ismini kiriting: "))
# print(dostlar)

# Amaliyot

# Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing, va ro'yxatdagi har bir
#  ismga takrorlanuvchi xabar yozing
# ismlar=['shuhrat','tolib','oybek',"o'tkir","nuriddin"]
# for ism in ismlar:
#   print(f"Assalomu alaykum, {ism.title()} salomatmisizlar?")
  
# # Yuoqirdagi tsikl tugaganidan so'ng, ekranga "Kod n marta takrorlandi" degan xabarni 
# # chiqaring (n o'rniga kod necha marta takrorlanganini yozing)
# print('Kod 5 marta takrorlandi')

# # 10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing. Ro'yxatning xar bir 
# # elementining kubini yangi qatordan konsolga chiqaring.
# sonlar=list(range(11,100,2))
# print(sonlar)
# for son in sonlar:
#     print(f"{son}ning kubi {son**3} ga teng")
    
# Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang, va kinolar degan 
# # ro'yxatga saqlab oling. Natijani konsolga chiqaring.
# kinolar=[]
# print("5 ta eng sevimli kinolaringiz qaysi?")
# for n in range(5):
#     kinolar.append(input(f"{n+1} - nomini kiriting: "))
# print(kinolar)

# Foydalanuvchidan bugun nechta odam bilan uchrashganini (suhbatlashganini) so'rang, 
# va har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga yozing. Ro'yxatni
# konsolga chiqaring.    
ismlar=[]
print("Bugun nechta odam bilan uchrashdingiz?")
for n in range(5):
    ismlar.append(input(f"{n+1} - ismni kiriting\n"))
print(ismlar)

