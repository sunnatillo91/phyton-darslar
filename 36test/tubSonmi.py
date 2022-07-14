# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 08:18:19 2022

Dasturlash asoslari

#35-DARS. DASTURNI TEKSHIRISH  tubSon test

Author: Sunnatillo Xayrullayev 
"""

# MANTIQIY QIYMATLARNI TEKSHIRISH

def tubSonmi(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False 
    for i in range(3, int(n**0.5)+1, 2):
        if n%i==0:
            return False
    return True
        
    
    
