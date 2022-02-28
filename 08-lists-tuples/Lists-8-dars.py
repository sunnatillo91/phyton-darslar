# 8-dars RO'YXATLAR LISTS
"""
Created on Wed Jan 12 14:21:09 2022
Dasturlash asoslari

@author: Sunnatillo Xayrullayev

"""

# #RO'YXATNI TARTIBLASH
# #Aksar holatlarda ro'yxat ichidagi elementlarni alifbo ketma-ketligida tartiblash 
# #talab qilinishi mumkin. Buning uchun list uchun maxsus .sort() metodidan foydalanamiz.
# cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
# cars.sort()
# print(cars)

# #Diqqat! Tartiblashda katta harflar kichik harflardan avval kelishini hisobga oling. Agar 
# #matndagi so'zlarning bosh harfi katta-kichik aralash yozilgan bo'lsa, ularni bir 
# #ko'rinishga keltirib olish maqsadga muvofiq bo'ladi.
# cars = ['Bmw','mercedes benz', 'volvo', 'gm', 'tesla', 'audi']
# cars.sort()
# print(cars)

# #Ro'yxatni teskari tartibda saqlash uchun .sort() metodi ichida reverse=True argumentini ham kiritamiz. 
# cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
# cars.sort(reverse=True)
# print(cars)

# #.sort() metodi ro'yxatni tartiblaydi. Ba'zida asl ro'yxat ichidagi elementlarning
# #ketma-ketligini buzmagan holda ro'yxatni tartiblash talab qilinishi mumkin. Buning uchun
# #sorted() funktsiyasidan foydalanamiz:
# mehmonlar = ['Odil', 'Hamid', 'Temur', 'Avazbek', 'Farruh', 'Shamsiddin']
# print("sorted() qaytargan ro'yxat:", sorted(mehmonlar))
# print("Asl ro'yxat o'zgarmas qoldi:", mehmonlar)
# #sorted() funktsiyasi yordamida teskari tartiblash uchun ham reverse=True argumentini beramiz:
# #Yuoqridagi ikki usul bilan sonli ro'yxatlarni ham tartiblashimiz mumkin:
# ages = [12, 98, 34, 65, 34, 76, 11]
# ages.sort()
# print(ages)
# print(sorted(ages, reverse=True))    

# #RO'YXATNI AYLANTIRISH
# #Ba'zida ro'yxatni aylantirish (boshini oxiriga, oxirini boshiga) talab qilinishi
# # mumkin. Buning uchun .reverse() metodidan foydalanamiz.
# fruits = ['pear','banana','apple','watermelon','lemon']
# fruits.reverse()
# print(fruits)

# #RO'YXATNING UZUNLIGINI BILISH
# #Ro'yxatning uzunligi, ya'ni uning ichidagi elementlar sonini aniqlash uchun len() funktsiyasidan foydalanamiz:
# fruits = ['pear','banana','apple','watermelon','lemon']
# print("Elementlar soni:",len(fruits)) # len(fruits) ro'yxat uzunligini qaytaradi

# #range() FUNKTSIYASI
# #Bu funktsiya yordamida biz ma'lum oraliqdagi sonlar ketma-ketligini yaratishimiz mumkin. 
# #list() funktsiyasi yordamida esa bu oraliqni ro'yxat shaklida saqlab olamiz:
# sonlar = list(range(0,10)) # 
# print(sonlar)

# #Diqqat! E'tibor qiling range() funktsiyasi ikkinchi indeksdan bitta avval to'xtaydi.
# #range() yordamida qadamni ham berishimiz mumkin:
# juft_sonlar = list(range(0,20,2)) # 0 dan 20 gacha 2 qadam bilan
# toq_sonlar = list(range(1,20,2))  # 1 dan 20 gacha 2 qadam bilan
# print("Juft sonlar: ", juft_sonlar)
# print("Toq sonlar: ", toq_sonlar)

# #Agar sonlar ketma-ketligi 0 dan boshlansa, range() funktsiyasida yakuniy indeksni 
# #ko'rsatish kifoya. Misol uchun range(0,10) emas range(10) deb yozsak ham bo'laveradi.

# sonlar1 =list(range(15))
# print(sonlar1)

# #SONLI RO'YXAT USTIDA SODDA AMALLAR
# #ro'yxatdagi eng kichik sonni topish uchun min() funktsiyasidan, eng katta sonni topish 
# #uchun esa max() funktsiyasidan, sonlarning yig'indisini topish uchun esa sum() funktsyasidan
# #foydalansak bo'ladi:

# narhlar = [12000, 22500, 23456, 9800, 5600, 9934, 32874]
# arzon = min(narhlar)
# qimmat = max(narhlar)
# jami = sum(narhlar)
# print("Eng arzon narh ", arzon, \
#       ". Eng qimmati ", qimmat, \
#           ". Jami: ", jami)
# #Agar kod uzun bo'lib ketsa, \ belgisi yordamida kodni yangi qatordan davom ettirish mumkin    

#RO'YXATNI KESISH
#Ba'zida ro'yxatning ma'lum bir bo'lagini ajratib olish talab qilinishi mumkin, deylik 
#biz quyidagi cars degan ro'yxatdan birinchi 3 ta elementni ajratib olmoqchimiz, buning 
#uchun biz boshlang'ich va oxirgi indekslarni beramiz:    

# cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
# my_cars = cars[0:3] # 0-indeskdan boshlab 3 ta element ajratib olamiz
# print(my_cars)     

# your_cars=cars[3:7]
# print(your_cars)    
# #Agar boshlang'ich indeksni bermasangiz, Python avtomat ravishda 0 indeksdan boshlab kesadi.
# #Agar 2-indeksni kiritmasangiz, ro'yxat oxirigacha kesadi:
# print(cars[:4]) # Ro'yxat boshidan 4-gacha kesadi (0,1,2,3)
# print(cars[2:]) # 2-elementdan boshlab ro'yxat oxirigacha kesib oladi

#RO'YXATDAN NUSXA OLISH

# sonlar = [1, 2, 3, 4, 5] # donlar degan ro'yxat yaratamiz
# sonlar2 = sonlar # sonlar2 degan ro'yxatni sonlar ga tenglaymiz
# sonlar2.append(6) # sonlar2 ga 6 sonini qo'shamiz
# sonlar2.append(7) # sonlar2 ga 7 sonini qo'shamiz
# print("Bu sonlar ro'yxati:", sonlar)
# print("Bu sonlar2 ro'yxati:", sonlar2)
# #Demak yuqorida biz sonlar2=sonlar deb yozgan komandamiz yangi ro'yxat yaratish o'rniga,
# #ikkala o'zgaruvchini ham bitta ro'yxatga bog'lab (yo'naltirib) qo'ydi. 
# #Biz sonlar yoki sonlar2 ustida bajargan amallarimiz aslida bitta ro'yxat ustida bajarilyapti.

# #Buning uchun yuoqirdagi ka'bi ro'yxatni kesish usulidan foydalanamiz. Faqatgina, 
# #kvadrat qavs ichida ikkala indeksni ham ko'rsatmasdan, bo'sh qoldiramiz:
# sonlar = [1, 2, 3, 4, 5] # donlar degan ro'yxat yaratamiz
# sonlar2 = sonlar[:] # [:] ro'yxatni to'liq ko'chirib oladi
# sonlar2.append(6) # sonlar2 ga 6 sonini qo'shamiz
# sonlar2.append(7) # sonlar2 ga 7 sonini qo'shamiz
# print("Bu sonlar ro'yxati:", sonlar)
# print("Bu sonlar2 ro'yxati:", sonlar2)

#TUPLES - O'ZGARMAS RO'YXAT
# Dastur yaratish davomida o'zgarmas ro'yxat tuzish talab qilinishi mumkin. 
# Pythonda bunday ro'yxatlar tuples deb yuritiladi. Tuple ichidagi qiymatlarni bir marta, 
# dastur boshida beriladi va so'ngra o'zgartirib bo'lmaydi. List dan farqli ravishda,
# Tuple e'lon qilishda kvadrat qavslar [] o'rniga oddiy qavslar () ishlatiladi:
# tomonlar = (20, 30, 55.2)
# print(tomonlar)
# toys=('bus','car','bear','dino','snake','lizrd')
# print(toys[1])
# print(toys[-1])

#Keling Tuple ichidagi biror elementning qiymatini o'zgartirib ko'ramiz:
#toys = ('bus','car','bear','dino','snake','lizard')
#toys[3] = 'dragon'
#Natija: TypeError: 'tuple' object does not support item assignment

# Agar Tuple ga o'zgartirish talab qilinsa, yagona yo'li o'zgarmas ro'yxatni list() 
# funktsiyasi yordamida List (oddiy ro'yxat) ko'rinishiga keltirib olish, o'zgarishlarni
# bajarsih va qaytarib tuple() funktsiyasi yordamida o'zgarmas ro'yxatga o'tkazish mumkin:
# o'zgarmas ro'yxat yaratamiz
# toys=('bus','car','bear','dino','snake','lizrd')
# print(toys)
# toys=list(toys) # o'zgarmas ro'yxatni oddiy ro'yxatga (List) aylantiramiz
# # Ro'yxatga o'zgartirishlar kiritamiz
# toys.append('dragon')
# toys.remove('bus')
# toys[1] = 'mcqueen'
# toys = tuple(toys) # Ro'yxatni qaytadan o'zgarmas ro'yxatga (Tuple) aylantiramiz
# print(toys)

#Amaliyot
#O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring
davlatlar=["o'zbekiston", "qozog'iston", "tojikiston", 'turkmaniston', "qirg'iziston"]
#print(davlatlar)

# #Ro'yxatning uzunligini konsolga chiqaring
# print(len(davlatlar))

# # sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring
# print(sorted(davlatlar))

# # sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring
# print(sorted(davlatlar, reverse=True))

# # Asl ro'yxatni qaytadan konsolga chiqaring
#print(davlatlar)

# # reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring
# davlatlar.reverse()
# print(davlatlar)

# # sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari 
# #tartibda konsolga chiqaring.
# davlatlar.sort()
# print(davlatlar)

# davlatlar.sort(reverse=True)
# print(davlatlar)

# 120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing
# juft_sonlar=list(range(120,1200, 2))

# # Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring
# jami=sum(juft_sonlar)
# print(jami)

# # Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang va konsolga chiqaring
# eng_katta=max(juft_sonlar)
# print(eng_katta)
# eng_kichik=min(juft_sonlar)
# print(eng_kichik)
# farq=eng_katta-eng_kichik
# print(farq)

# # Ro'yxatdagi elementlar sonini hisoblang
# print(len(juft_sonlar))

# # Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring
# r_boshi=juft_sonlar[0:20]
# r_ortasi=juft_sonlar[530:550]
# r_oxiri=juft_sonlar[-20:]
# print(r_boshi)
# print(r_ortasi)
# print(r_oxiri)

# # taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting
# taomlar=['osh','somsa','baliq','shashlik','jiz']

# # nonushta degan yangi ro'yxatga taomlardan nusxa oling
# nonushta=taomlar[:]

# # Yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring, 
# # va qo'shimcha 2 ta taom qo'shing
# nonushta.remove('osh')
# nonushta.remove('somsa')
# nonushta.remove('jiz')
# print('nonushtaga yeyiladigan taomlar', nonushta)
# nonushta.append('akula jigari')
# nonushta.append('qaymoq')
# # print(nonushta)

# # Ikkala ro'yxatni ham (taomlar va nonushta) konsolga chiqaring
# print(taomlar)
# print(nonushta)

# # Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring va nonushta[0] = "qaymoq va non" deb qiymat berib ko'ring.
# nonushta=tuple(nonushta)
# print(nonushta)
# # nonushta[0]='qaymoq va non'



