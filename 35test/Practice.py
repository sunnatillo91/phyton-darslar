# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 11:48:15 2022

#35-DARS. DASTURNI TEKSHIRISH  practice

Author: Sunnatillo Xayrullayev
"""

# 1  Katta son

def sonKattami(a, b, c):
    """Sonlardan kattasini topuvchi funksiya"""
    if a>b>c : return a
    if b>a>c: return b
    else: return c
    
print(sonKattami(3, 6, 9))
    

# 2  Matnlardan iborat ro'yxat qabul qilib, ro'yxatdagi har bir matnning birinchi harfini katta harfga 
# o'zgatiruvchi funksiya

def getMatn(intro, body, conclusion = ''):
    if conclusion:
        return f"{intro} {body} {conclusion}".title()
    else:
        return f"{intro} {body}".capitalize()

print(getMatn("sunnatilloning dasturlashdagi hayot yo'li", "dastlab hamkasbi, so'ngra kutubxonada uchragan \
Anvar Narzullayevning dasturlash asoslari haqidagi kitobi uning dasturlash sohasiga kirib \
kelishiga sabab bo'ldi"))

