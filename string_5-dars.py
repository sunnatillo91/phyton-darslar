# 05-dars String(Matan)
"""
Created on Sun Jan  9 08:43:58 2022

@author: Sunnatillo
"""

#viloyat = 'Фарғона'
#avto = 'Nexia 3'
#matn = 'danduning ertalabki holati 🙂'
#matn="Men yangi 📱 oldim"
#print(matn)
#belgilar, emojilar vab. topish uchun sayt https://unicode-table.com

# String ustida amallar

#ism= 'Ahmad'
#print("Uning ismi" ' '+ ism)
#familiya= 'Xayrullayev'
#ism="Sunnatillo"
#print(ism+' ' +familiya)

# f-string ikki va undan ko'p matn ko'rinishdagi o'zgaruvchilarni birlashtiradi

#ism_sharif=f'{ism} {familiya}'
#print(f'{ism} {familiya}')
#fname="James"
#lname="Bond"
#matn = f"Salom, mening ismim {lname}. {fname} {lname}!"
#print(matn)
#tyil=1966
#print(f"Siz {tyil}-da tug'ilgansiz.")
#print(f"Yoshingiz {2021-tyil} da")

# MAXSUS BELGILAR

#print("Helllo \tworld!") # \t - bo'sh joy qo'shish
#print("Helllo \nworld!")  # \n - qator tashlash 

# STRING METODLAR

#ism = "james"
#familiya = "bond"
#ism_sharif = f"{ism} {familiya}"
#ism_sharif = ism_sharif.upper() # Agar o'zgaruvchini ichidagi qiymatni o'zgartirmoqchi bo'lsak
#print(ism_sharif.upper())
#print(ism_sharif.lower())
#print(ism_sharif.title())
#print(ism_sharif.capitalize())

#meva = "    olma        "    # meva = meva.strip()
#print("Men " + meva.lstrip() + " yaxshi ko'raman")     
#print("Men " + meva.rstrip() + " yaxshi ko'raman")  
#print("Men " + meva.strip() + " yaxshi ko'raman")        
#ism = input("Ismingiz nima?")
#print("Assalomu alaykum, " + ism)
#ism = input("Ismingiz nima?\n") # Foydalanuvchi ismini yangi qatorga o'tkazish
#print("Assalomu alaykum, " + ism.title())

# AMALIYOT
#1 Quyidagi o'zgaruvchilarni yarating
kocha = "Bog'bon"
mahalla="Sag'bon"
tuman="Bodomzor"
viloyat="Samarqand"
#2 Yuqoridagi o'zgaruvchilarni jamlab konsolga chiqaring
# Diqqat uzun kodlarni \ belgisi yordamida keyingi qatorga ko'chirish mumkin
print(kocha+ " ko'chasi, " + mahalla + " mahallasi, " + \
      tuman + " tumani, " + viloyat + " viloyati")
#3 Yuqoridagi o'zgaruvchilarning qiymatini foydalanuvchidan so'rang va avvalgi mashqni takrorlang
kocha = input("ko'changiz nomi?\n")
mahalla=input("Mahallangiz nomi?\n")
tuman=input("tumaningiz nomi?\n")
viloyat=input("Viloyatingiz nomi?\n")
#print(f"{kocha} ko'chasi,\n{mahalla} mahallasi,\n{tuman} tumani,\n{viloyat} viloyati")
#4 Yuqoridagi matnni konsolga chiqarishda har bir verguldan keyin yangi qatordan yozing
print(kocha+ " ko'chasi, " + mahalla + " mahallasi, " + \
      tuman + " tumani, " + viloyat + " viloyati")
#5 Yuqoridagi matnni f-string yordamida yangi, manzil deb nomlangan o'zgaruvchiga yuklang
manzil = f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati"
manzil= manzil.title()
#6 manzilga biz yuqorida o'rgangan title(), upper(), lower() , capitalize() metodlarini qo'llab ko'ring
print(manzil.title())
print(manzil.upper())
print(manzil.lower())
print(manzil.capitalize())