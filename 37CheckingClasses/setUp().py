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
        self.avto1 = Car(make,model,year,price=self.price)
        
    def test_create(self):
        self.assertIsNotNone(self.avto1.make)
        self.assertIsNotNone(self.avto1.model)
        self.assertIsNotNone(self.avto1.year)
        self.assertIsNone(self.avto1.price)
        self.assertEqual(0, self.avto1.get_km())
        self.assertEqual(self.price,self.avto2.price)
        
unittest.main()
        