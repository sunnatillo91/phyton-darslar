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

# 3  Berilgan sonlar ro'yxatidan juft sonlarni ajratib oluvchi funksiya

def sonJuftmi(n):
    if n==0: return True
    if n%2==0: return True
    else: return False
    
print(sonJuftmi(16))
print(sonJuftmi(206))


# 4  Berilgan son Fibonachchi ketma-ketligida uchraydimi (True) yoki yo'q (False) \
#    qaytaruvchi funksiya yozing.

n = int(input("Istalgan son kiriting: "))
a=0
b=1
c=0

for x in range(n):
    print(c, end=" ")
    c=a+b
    b=a
    a=c
    
def sonFibonachchimi(x, n):
    if n in x: return True
    else: return False
    
print(sonFibonachchimi(5, 8))
    
    