# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 19:26:53 2022

Dasturlash asoslari

39-dars TASHQI KUTUBXONALAR
                    
@author: Sunnatillo Xayrullayev
"""

from googletrans import Translator
tarjimon = Translator() # Translator bu maxsus klass (tarjimon esa obyekt)

matn_uz = "Python - dunyodagi eng mashxur dasturlash tili"
# Istalgan matnni ingliz tiliga tarjima qilish uchun translate metodini chaqiramiz

# Original matn
print(tarjimon.origin)

#Tarjima
tarjima = tarjimon.translate(matn_uz)
print(tarjima.text)

#Original matn tili
print(tarjimon.src)













