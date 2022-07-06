# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 16:32:32 2022

Dasturlash asoslari

#34-DARS. JSON Practise

Author: Sunnatillo Xayrullayev
"""
import json

# 1
data = {"Model" : "Malibu", "Rang" : "Qora", "Yil" : 2020, "Narx" : 40000}
data_json = json.dumps(data)
print(data_json)

# 2
talaba_json = """{"ism":"Hasan", "familiya":"Karimov", "tyil":1999}"""
talaba = json.loads(talaba_json)
print(f"{talaba['ism']} {talaba['familiya']} ")

#3
with open('javoblar/talaba.json', 'w') as f:
    json.dump(talaba, f) 
    
    
with open('javoblar/data.json', 'w') as f:
    json.dump(data, f)

#4 students

with open('javoblar/students.json', 'w') as f:
    talabalar = json.load(f)

