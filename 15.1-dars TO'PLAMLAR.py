"""
Created on Wed Jan 20 08:52:38 2022

Dasturlash asoslari

15.1-dars Dictionary (Lug'at) lar bilan ishlash
                    
@author: Sunnatillo Xayrullaev
"""

# TO'PLAMLAR
# To'plamdan element o'chirish uchun .discard() va .remove() metodlari mavjud. 
mevalar = {'anjir','olma','uzum','banan','anor'}
mevalar.discard('anjir')
print(mevalar)
mevalar.remove('banan')
print(mevalar)

# Yuqoridagi 2 ta metod vazifasi bir xil, farqi .remove() metodi xato qaytaradi, .discard() esa xato qaytarmaydi

# sonlar = {1,2,3,4,5,6}
# sonlar.discard(7)  # to'plamda 7 yo'q
# print(sonlar)
# sonlar.remove(7)
# KeyError: 7

# TO'PLAMLAR USTIDA AMALLAR. ikki to'plamni birlashtirish uchun | operatori yoki .union() metodidan foydalanamiz.

A = {1,2,3,4}
B = {3,4,5,6}
C = A|B
print(C)

D = A.union(B)
print(D)

# iKKI TO'PLAM KESISHMASINI(BIR XIL ELEMENTLARINI) TOPISH uchun & operatori yoki .intersection() metodidan foydalaniladi.

A = {1,2,3,4}
B = {3,4,5,6}
print(A&B)
{3, 4}  # A va B uchun umumiy elementlar
print(A.intersection(B))
{3, 4}    
      
# Ikki to'plam o'rtasidagi farqni topish uchun, - operatori yoki .differnce() metodidan foydalaniladi.


A = {1,2,3,4}
B = {3,4,5,6}
print(A-B)      
{1, 2} # A da bor B da yo'q

print(B.difference(A))      
{5, 6}  # B da or A da yo'q

# To'plamlar o'rtasidagi simmetrik farqni topish ^ operatoridan yoki .symmetric_difference() metodidan foydalanamiz
print(A^B)
{1, 2, 5, 6}
print(A.symmetric_difference(B))


# AMALIYOT
# 1
ranglar = {'yashil','sariq','qizil'}
ranglar.add("ko'k")
ranglar.update('oq','kulrang')
{'l', 'q', 'n', 'sariq', 'qizil', 'o', 'a', 'u', 'r', 'k', 'g', "ko'k", 'yashil'}
print(ranglar)

# 2
set1 = {10,20,30,40,50}
set2 = {30,40,50,60,70}
set = set1&set2 or set1.intersection(set2)
print(set)

# 3
print(set1-set2)
print(set2.difference(set1))

# 4
print(set1^set2)
print(set2.symmetric_difference(set1))

# 5
bozorlik = ['choy','non','kartoshka','tuxum','sut']
maxsulotlar = ['non','sut','tuxum','olma','un','tuz']

mavjud_maxsulotlar = []
mavjud_emas = []
for m in bozorlik:
    if m in maxsulotlar:
        # print(m)
        mavjud_maxsulotlar.append(m)
    else:
        mavjud_emas.append(m)
        print(m)
        maxsulotlar.append(m)
print(maxsulotlar)        

