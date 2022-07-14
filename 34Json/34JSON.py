# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 19:32:44 2022

Dasturlash asoslari

#34-DARS. JSON

Author: Sunnatillo Xayrullayev
"""

# Pythondan JSON ga

#json dumps()

import json
x=10
x_json = json.dumps(x)
ism = "sunnatillo"
ism_json = json.dumps(ism)
sonlar = [12,45,35,64,89]
sonlar_json = json.dumps(sonlar)

bemor = {
    "ism":"Alijon Valiyev",
    "yosh":30,
    "oila":True,
    "farzandlar":("Abdulloh", "Umar"),
    "allergiya": None,
    "dorilar": [
        {"nomi": "Analgin", "miqdori":0.5},
        {"nomi": 'Panadol', "miqdori":1.2}
        ]
    }
bemor_json= json.dumps(bemor)
print(bemor_json)

bemor_json = json.dumps(bemor, indent = 4)
print(bemor_json)

# json.dump()

bemor = {
    "ism":"Alijon Valiyev",
    "yosh":30,
    "oila":True,
    "farzandlar":("Abdulloh", "Umar"),
    "allergiya": None,
    "dorilar": [
        {"nomi": "Analgin", "miqdori":0.5},
        {"nomi": 'Panadol', "miqdori":1.2}
        ]
    }
with open('bemor.json', 'w') as f:
    json.dump(bemor, f, indent = 4)
    
# JSONDAN PYTHONGA
# json.loads()

sonlar = json.loads(sonlar_json)
bemor = json.loads(bemor_json)
print(bemor)

# json.load()

filename = 'bemor.json'
with open(filename) as f:
    bemor = json.load(f)

print(type(bemor))
    
    
    