"""
Created on Mon Feb 21 21:26:40 2022

Dasturlash asoslari

26-dars "SO'Z TOPISH" O'YINI сodes
"""

from uzwords import words
# print(words[453])
import random as r

def get_word():
    word = r.choice(words)
    while "-" in word or " " in word:
        word=r.choice(words)
    return word.upper()

def display(user_letters, word):
    display_letter=''
    for letter in word:
        if letter in user_letters.upper():
            display_letter+=letter
        else:
            display_letter+='-'        
    return display_letter   
        
def play():
    word=get_word()
    # so'zdagi harflar
    word_letters=set(word)
    # foydalanuvchi kiritgan harflar
    user_letters=''
    print(f"Men {len(word)} xonali so'z o'yladim topa olasizmi? ")
    # print word
    while len(word_letters)>0:
        print(display(user_letters, word))
        if len(user_letters)>0:
            print(f"shu vaqtgacha kiritgan harflaringiz: {user_letters}")
            
        letter = input("Harf kiriting: ").upper()
        if letter in user_letters:
            print("Avval bu harfni kiritgansiz, boshqa harf kiriting")
            continue
        elif letter in word:
            word_letters.remove(letter)
            print(f"{letter} harfi to'g'ri")
        else:
            print("Bunday harf yo'q")
        user_letters+=letter 
    print(f"Tabriklayman! {word} so'zini {len(user_letters)} ta urinishda topdingiz")    
        
    