
"""
Created on Tue Jul 26 19:15:29 2022

Dasturlash asoslari

#38-DARS. KUTUBXONALAR  RegEx

Author: Sunnatillo Xayrullayev
"""


# RegEx - ANDOZA YORDAMIDA MATN IZLASH  regular expressions

import re
from uzwords import words

word1 = "темир"
word2 = "томир"
word3 = "тулпор"

andoza = "^т...р$"
print(re.match(andoza, word1))
print(re.match(andoza, word2))
print(re.match(andoza, word3))

andoza = "^а.....т$"
matches = []
for word in words:
    if re.match(andoza,word):
        matches.append(word)
       
print(matches)

eandoza = '[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'
matn = """Maqolalar  2020-yilning 20-martiga qadar rtmkonferensiya2021@mail.ru elektron pochtasida qabul qilinadi.
Quyidagi yo'nalishdagi maqolalar qabul qilinadi:
👉 Aniq va tabiiy fanlarni zamonaviy pedagogik texnologiyalar asosida o‘qitish  metodikasi.
👉 Umumta’lim  fanlarini o‘qitishda  STEAM yondashuvning o’rni va ahamiyati. """
email = re.findall(eandoza, matn)
print(email)


# kuchli parolni tekshirish
