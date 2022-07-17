# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 09:52:36 2022

#37-DARS. СLASSLARNI TEKSHIRISH setUp()

Author: Sunnatillo Xayrullayev
"""

# setUp() METODI
import unittest
from cars import Car

class CarTest(unittest.TestCase):
    """Car classini tekshirish uchun test"""
    def setUp(self):
        make = "GM"
        model = "Malibu"
        year = 2021
        self.price = 40000
        self.km = 1000
        self.avto1 = Car(make,model,year)
        self.avto2 = Car(make,model,year,price=self.price)
        
    def test_create(self):
        # avto1 obyektini km va narxini bermasdan yaratmiz
        avto1 = Car("toyota", "camry", 2021)
        # assertIsNotNone() qiymat mavjudligini tekshiradi
        self.assertIsNotNone(avto1.make)
        self.assertIsNotNone(avto1.model)
        self.assertIsNotNone(avto1.year)
        # assetrtIsNone qiymat mavjud emasligini tekshiradi
        self.assertIsNone(avto1.price)
        # assertEquals qiymatlar tengligini tekshiradi
        self.assertEqual(0, avto1.get_km())
        # Yangi obyekt yaratamiz va narxini ham ko'rsatamiz
        avto2 = Car("toyota", "camry", 2020, price=75000)
        self.assertEqual(75000, avto2.price)
        
    def test_set_price(self):
        self.avto2.set_price(self.price)
        self.assertEqual(self.price, self.avto2.price)
    
    def test_add_km(self):
        #1 musbat qiymat berib ko'ramiz
        self.avto1.add_km(self.km)
        self.assertEqual(self.km, self.avto1.get_km())
        self.avto1.add_km(5000)
        self.assertEqual(6000, self.avto1.get_km())
        #2 manfiy qiymat berib ko'ramiz
        new_km = -5000
        
        try:
            self.avto1.add_km(new_km)
        except ValueError as error:
            self.assertEqual(type(error), ValueError)
            
    def test_get_info(self):
        avto1_info = 'GM Malibu, 2021-yil, 20000km yurgan. Narxi: 50000'
        
        self.avto1.add_km(20000)
        self.assertEqual(20000, self.avto1.get_km())
        self.avto1.set_price(50000)
        self.assertEqual(avto1_info, self.avto1.get_info())
        
unittest.main()