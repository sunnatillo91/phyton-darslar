# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 20:01:48 2022

Dasturlash asoslari

25-dars "SON TOPISH" O'YINI сodes
"""

import random as r     

def son_top(x=10):
    tasodifiy_son = r.randint(1, x)
    print(f"1 dan {x} gacha son o'yladim topa olasizmi?: ")
    taxminlar=0
    while True:
        taxminlar+=1
        taxmin = int(input(" "))
        if taxmin<tasodifiy_son:
            print("Xato, men o'ylagan son bundan kattaroq. Yana harakat qiling: ")
        elif taxmin>tasodifiy_son:
            print("Xato, men o'ylagan son bundan kichikroq. Yana harakat qiling: ")
        else:
            break
        
    print(f"Topdingiz! {taxmin} sonini o'ylagandim."
          f"{taxminlar} ta taxmin bilan topdingiz. Tabriklayman!") 
    return taxminlar


def son_top_pc(x=10):
    input(f"1 dan {x} gacha son o'ylang topishga harakat qilaman.Son o'ylagan bo'lsangiz istalgan tugmani bosing ")
    quyi = 1
    yuqori = x      
    taxminlar_pc=0
    while True:
        taxminlar_pc+=1
        if quyi!=yuqori:
            taxmin_pc = r.randint(quyi,yuqori)
        else:
            taxmin_pc=quyi
        javob=input(f"Siz {taxmin_pc} sonini o'yladingiz: to'g'ri (t): , men o'ylagan son bundan kattaroq (+): , \
                    kichikroq (-): ".lower())
        if javob=='-':
            yuqori=taxmin_pc-1
        elif javob=='+':
            quyi=taxmin_pc+1
        else:
            break
    print(f"{taxminlar_pc} ta taxmin bilan topdim!")
    return taxminlar_pc
   
def play(x=10):
    yana = True
    while yana:
        taxminlar_pc = son_top_pc(x)
        taxminlar_user = son_top(x)
        
        if taxminlar_user>taxminlar_pc:
            print("Men yutdim")
        elif taxminlar_user<taxminlar_pc:
            print("Siz yutdingiz")
        else:
            print("Durrang!")
            
        yana = int(input("Yana o'ynaysizmi?: ha(1)/ yo'q(0)"))    
            
    