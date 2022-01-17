# 7-dars RO'YXATLAR LISTS
"""
Created on Mon Jan 10 23:15:24 2022

Dasturlash asoslari

@author: S.Khayrullaev
"""

mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]
narxlar = [12000, 18000, 10900, 22000]
sonlar = ['bir', 'ikki', 3, 4, 5]  # aralsh ro'yxat
ismlar = []  # bo'sh ro'yxat

# RO'YXAT ELEMENTLARI
print("Birinchi meva: ", mevalar[0])
print("Ikkinchi meva: ", mevalar[1])
print("Oxirgi meva: ", mevalar[3])  # yoki print("Oxirgi meva: ", mevalar[-1]) 

print("Birinchi meva: ", mevalar[0].title())
print("Ikkinchi meva: ", mevalar[1].upper())
print("Oxirgi meva: ", mevalar[3].capitalize())

print(narxlar[2]+narxlar[3])

sonlar = [10,25,12,45,34,-45,38,-33]
print(sonlar[-1])   # listning oxirgi elementiga -1 orqali ham murojaat qilish mumkin

# ELEMENTLARNI QO'SHISH, O'CHIRISH, VA O'ZGARTIRISH
# Elementni o'zgartirish
narxlar = [12000, 18000, 10900, 22000]
narxlar[0]=13000 #1-qiymatni 13000 ga o'zgartiramiz
narxlar[2]=11000 #3-qiymatni 11000 ga o'zgartiramiz
narxlar[3]=narxlar[3]+2000 #4-qiymatga 2000 qo'shamiz
print(narxlar)

#Yangi element qo'shish
mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]
mevalar.append("tarvuz") # mevalarga tarvuz qo'shamiz
print(mevalar)

cars = [] #bo'sh ro'yxat yaratamiz
cars.append('Lacetti') # royxatga Lacetti qo'shamiz
cars.append('Nexia 3') # royxatga Nexia 3 qo'shamiz
cars.append('Cobalt') # royxatga Cobalt qo'shamiz
print(cars)

cars = ['Lacetti', 'Nexia 3', 'Cobalt']
cars.insert(0, 'Malibu')
print(cars)
cars.insert(-2, 'Damas')
print(cars)

# Elementni o'chirish
mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]
del mevalar[1] # 2-element 'anjir' ni o'chirib tashlaymiz
print(mevalar)

mevalar.remove('shaftoli') # ro'yxatdan shaftolini o'chirdik
print(mevalar)

hayvonlar = ['it', 'mushuk', 'sigir', 'quyon', 'mushuk']
hayvonlar.remove('mushuk')  #ikki va undan ortiq bir xil qiymatli elementdan faqat 1-sini o'chiradi 
print(hayvonlar)

# Elementni sug'urib olish
bozorlik = ["yog'", "un", "piyoz", "banan", "go'sht"]
maxsulot = bozorlik.pop(3)  # 4-elementni sug'urib olamiz
print("Men " + maxsulot + " sotib oldim")
print("Olinmagan maxsulotlar: ", bozorlik)

numbers = [1,2,3,4,5]
print(numbers)
numbers.pop()  # bu metodda index berilmasa ro'yxatdagi oxirgi qiymatni sug'urib oladi
print(numbers)

# AMALIYOT
#1 ismlar degan ro'yxat yarating va kamida 3 ta yaqin do'stingizning ismini kiriting
ismlar = ["Shuxrat", "Oybek", "O'tkir"]
#2 Ro'yxatdagi har bir do'stingizga qisqa xabar yozib konsolga chiqaring:
xabar = "Assalomu alaykum, Shuxrat do'stim yaxshimisan?"
xabar2 = "Oybek va O'tkir do'stlar nima bilan bandsilar?"
print(xabar)
print(xabar2)
#3 sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni yuklang (musbat, manfiy, butun, o'nlik). 
sonlar = [52,-45,35,3.14]
print(sonlar)
#4 Yuqoridagi ro'yxatdagi sonlar ustida turli arifmetik amallar bajarib ko'ring. 
#Ro'yxatdagi ba'zi sonlarning qiymatini o'zgartiring, ba'zilarini esa almashtiring. 
print(sonlar[0]+sonlar[1]+sonlar[-1])
print(sonlar[-2]-sonlar[3])
print(sonlar[1]*sonlar[2])
print(sonlar[-3]/sonlar[0])

sonlar.append(39)
sonlar.append(42)
sonlar.insert(2, -21)
sonlar.insert(-1, 52)
print(sonlar)    
sonlar[2]=31
sonlar[-1]= 57
print(sonlar)

#5 t_shaxslar va z_shaxslar degan 2 ta ro'yxat yarating va biriga o'zingiz eng
#ko'p hurmat qilgan tarixiy shaxslarning, ikkinchisiga esa zamonamizdagi tirik
#bo'lgan shaxslarning ismini kiriting
t_shaxslar = ["Muhammad alayhissalom", 'Abubakr siddiq', 
'Hazrati Umar','Hazrati Usmon', "Hazrati Ali"]
z_shaxslar = ['Shayx Muhammad Sodiq', 'Mubashshir domla', 'Ilon Musk']
# Yuqoridagi ro'yxatlarning har biridan bittadan qiymatni sug'urib olib 
#(.pop()), quyidagi ko'rinishda chiqaring:

print("Men tarixiy shaxslardan " + t_shaxslar.pop(0) + " bilan, " 
"\nzamonaviy shaxslardan esa " + z_shaxslar.pop(1) + " bilan \nsuhbat qilishni istardim")

#friendsnomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta 
#mehmonga chaqirmoqchi bo'lgan do'stlaringizni kiriting. 
friends = []
friends.append("Adham")
friends.append("Nurjahon")
friends.append("Olmos")
friends.append("Akrom")
friends.append("Hikmat")
friends.append("Shuhrat")
print(friends)

#Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() 
#metodi yordamida o'chrib tashlang. 
friends.remove("Adham")
friends.remove("Olmos")

# Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing
friends.insert(0, "Oybek")
friends.insert(-3, "Tolib")
friends.insert(-1, 'Nuriddin')
print(friends)

# Yangi mehmonlar deb nomlangan bo'sh ro'yxat yarating. .pop() va .append() 
#metodlari yordamida mehmonga kelgan do'stlaringizning ismini friends 
#ro'yxatidan sug'urib olib, mehmonlar ro'yxatiga qo'shing.
Yangi_mehmonlar = []
kelolmaganlar = friends.pop(3)
kelolmaganlar = friends.pop(-3)
Yangi_mehmonlar.append(friends)
print(Yangi_mehmonlar)
