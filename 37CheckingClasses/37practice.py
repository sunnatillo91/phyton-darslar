"""
Created on Sun Jul 17 17:42:06 2022

#37-DARS. СLASSLARNI TEKSHIRISH PRACTICE

Author: Sunnatillo Xayrullayev
"""
#1

import unittest
from Inheritance import Shaxs, Talaba, manzil

class ShaxsTest(unittest.TestCase):
    """Shaxs classini tekshirish uchun test"""
    def setUp(self):
        ism = "Sunnatillo"
        familiya = "Xayrullayev"
        pasport = "AA459566"
        self.tyil = 1991
        self.inson = Shaxs(ism, familiya, pasport, tyil=self.tyil)
        
    def test_create(self):
        self.assertIsNotNone(self.inson.ism)
        self.assertIsNotNone(self.inson.familiya)
        self.assertIsNotNone(self.inson.pasport)
        self.assertIsNotNone(self.inson.tyil)
        
    def test_get_age(self):
        self.inson.get_age(2022)
        self.assertEqual(2022-self.tyil, self.inson.get_age(2022))
        
    def test_get_info(self):
        inson_info = "Sunnatillo Xayrullayev. Pasport: AA459566, 1991-yilda tug'ilgan"
        self.assertEqual(inson_info, self.inson.get_info())
        
        

class TalabaTest(unittest.TestCase):
    """Talaba klassini tekshirish uchun test"""
    def setUp(self):
        ism = "Sunnatillo"
        familiya = "Xayrullayev"
        pasport = 'AB456523'
        tyil = 2001
        self.idraqam = id
        self.bosqich = 1
        self.manzil = manzil
        self.talaba = Talaba(ism,familiya,pasport,tyil,id,manzil)
        
    def test_create(self):
        self.assertIsNotNone(self.talaba.ism)
        self.assertIsNotNone(self.talaba.familiya)
        self.assertIsNotNone(self.talaba.pasport)
        self.assertIsNotNone(self.talaba.tyil)
        self.assertIsNotNone(self.talaba.idraqam)
        self.assertEqual(1, self.talaba.bosqich)
        
    def test_get_id(self):
        self.talaba.get_id()
        self.assertEqual(self.idraqam, self.talaba.get_id())
        
    def test_get_bosqich(self):
        self.talaba.get_bosqich()
        self.assertEqual(self.bosqich, self.talaba.get_bosqich())
        
unittest.main()

# 2
