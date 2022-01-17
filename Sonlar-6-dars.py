# 06-dars Sonlar
"""
Created on Mon Jan 10 19:17:35 2022

Dasturlash asoslari

@author: S.Khayrullaev
"""

a = 20
b = 5.5
temp = -36.6
#print(type(a))
aholi_soni = 7_594_376_567
print("Aholi soni: ", aholi_soni)

c = a*b

d = 100//2
print(d)

# Kvadratning yuzini hisoblaymiz
kvdrt_tmni = 20 # kvadrat tomoni 20 ga teng
kvdrt_yuzi = kvdrt_tmni**2 # Kvadrat yuzini hisoblaymiz
print(kvdrt_yuzi)

# FLOATS

PI = 3.14159 # o'nlik son (float) konstanta
radius = 10 # butun son (integer)
diametr = 2*radius
print("Aylana uzunligi ", PI*diametr, " ga teng.")

a=-20
b=40
c=b/a
print(c)  # natija o'nlik bo'ladi

# BUTUN SONDAN O'NLIK SONGA
a=2  #butun son
b=3.0  # o'nlik son
print(a+b)  # natija o'nlik bo'ladi
print(a*b)
print(a**b)

# BIR NECHTA O'ZGARUVCHIGA QIYMAT BERISH

x, y, z = 20, 5.5, -56

#yosh, ism = 36, 'Olimjon'
#print(f"{ism.title()} {yosh} yoshda")

# O'ZGARUVCHINI ALMASHTIRISH
ism = "Jobir"
#yosh=36
#xabar = ism + ' ' + str(yosh) + ' yoshda'
#print(xabar)

#O'ZGARUVCHI TURINI TEKSHIRISH
print(type(ism))
#print(type(yosh))

#INPUT() VA SONLAR

#1 foydalanuvchining tug'ilgan yilini so'raymiz
#t_yil = int(input("Tug'ilgan yilingizni kiriting: "))
#2 foydalanuvchi yoshini hisoblaymiz
#yosh = 2022 - t_yil #
#3 foydalanuvchi yoshini konsolga chiqaramiz
#print("Siz ", yosh, " yoshda ekansiz")
#print("Siz " + str(yosh) + " yoshda ekansiz")

#1.1 foydalanuvchining tug'ilgan yilini so'raymiz
#t_yil = input("Tug'ilgan yilingizni kiriting: ")
#1.2 t_yil o'zgaruvchini int ga aylantiramiz
#t_yil = int(t_yil)
#2 foydalanuvchi yoshini xisoblaymiz
#yosh = 2022 - t_yil # 
#3 foydalanuvchi yoshini konsolga chiqaramiz
#print("Siz " + str(yosh) + " yoshda ekansiz")

a = int("10")
b = float("10")
temp = str(36.6)

#AMALIYOT
#Quyidagi dasturlarning har birini alohida fayl ko'rinishida yozing va bajaring:
 #1 Foydalanuvchi kiritgan sonning kvadrati va kubini konsolga chiqaruvchi dastur
#son = input("Istalgan son kiriting\n")
#son = int(son)
#print(son**2)  
#print(son**3)  
#2 Foydalanuvchining yoshini so'rab, uning tug'ilgan yilini hisoblab, konsolga chiqaruvchi dastur
yosh = int(input("Yoshingiz: \n"))
t_yil = 2022 - yosh
#print("Siz", t_yil, "yilda tug'ilgansiz")
#3 Foydalanuvchidan ikki son kiritshni so'rab, kiritilgan sonlarning yig'indisi, ayirmasi, ko'paytmasi va bo'linmasini chiqaruvchi dastur
a = int(input("1-sonni kiriting\n"))
b = int(input("2-sonni kiriting\n"))
print(f"{a}+{b} =", a+b)
print(f"{a}-{b} =", a-b)
print(f"{a}*{b} =", a*b)
print(f"{a}/{b} =", a/b)
