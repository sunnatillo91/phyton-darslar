# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 15:13:22 2022

Dasturlash asoslari

#38-DARS. KUTUBXONALAR  MATH

Author: Sunnatillo Xayrullayev
"""

import math

PI = math.pi
print(f"pi ning qiymati: {PI}")

E = math.e
print(f"e ning qiymati: {E}")


# Trigonometriya

a = math.sin(math.pi/2)
print(a)

b = math.cos(0)
print(b)

math.tan(PI)

# Burchaklar va radianlar o'rtasida konvertatsiya

print(math.degrees(math.pi/2))
print(math.radians(90))

# Logarifmlar
# Natural logorifm

print(math.log10(1000))
print(math.log(5))

# Sonlarni yaxlitlash

a = 4.6
print(math.ceil(a))     # Yuqoriga yaxlitlash
print(math.floor(a))    # Pastga yaxlitlash
print(round(a))         # Eng yaqin songa yaxlitlaydi

# Kvadrat ildiz
print(math.sqrt(81))

# Darajaga oshirish

print(math.pow(a, 3))   # a ning 3-darajasi
print(math.pow(a, 5))   # a ning 5-darajasi
print(math.pow(a, 1/3))     # a ning kub ildizi
