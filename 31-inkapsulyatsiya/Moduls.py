# KLASSLARNI MODULGA AJRATISH

# Vaqt o'tishi bilan dasturimizda klasslar ko'payib borishi tabiiy. Bizning asosiy dasturimiz 
# uzun va chigal bo'lmasligi uchun klasslarni ham huddi funksiyalar kabi alohida modullarga 
# ajratish maqsadga muvofiq bo'ladi. Dastur davomida kerak bo'ladigan klasslarga esa modulni
#  chaqirish (import) orqali murojat qilishimiz mumkin. Bunda, bir-biriga bog'liq klasslarni 
# bitta faylga joylashimiz mumkin. Misol uchun, biz Talaba, Professor, Foydalanuvchi va Shaxs
# degan klasslarni bitta odamlar.py moduliga, Avto, Bus, Train degan klasslarni esa boshqa
# transport.py moduliga joyladik. Kelajakda biz bu klasslarga import orqali murjat qilishimiz mumkin.


# Bitta klassni import qilish


from avto import Avto

avto1 = Avto("GM", "Malibu", "Qora", 2020, 40000)
avto2 = Avto("GM", "Lacetti", "Oq", 2020, 20000)
avto3 = Avto("Toyota", 'Carolla', "Silver", 2021, 35000)

print(Avto.get_num_avto())

# Bir nechta klasslarni import qilish

from avto import Avto, Bus

avto1 = Avto("GM", "Malibu", "Qora", 2020, 40000)
avto2 = Avto("GM", "Lacetti", "Oq", 2020, 20000)


# Modulning o'zini chaqirish

import avto

avto3 = avto.Avto("Toyota", 'Carolla', "Silver", 2021, 35000)

# Moduldagi barcha klasslarni impport qilish

from avto import *

# bu usul tavsiya qilinmaydi. Sababi moduldagi qaysi klassdan foydalanganimizni bir qarashda bilish qiyin 
# undagi klasslar va iz yaratgan klasslar nomi bir xil bo'lsa dastur xato ishlaydi


