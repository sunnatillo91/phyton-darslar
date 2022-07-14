# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 12:47:39 2022

Dasturlash asoslari

#35-DARS. DASTURNI TEKSHIRISH  test

Author: Sunnatillo Xayrullayev 
"""

import unittest
from name import get_fullname

class NameTest(unittest.TestCase):
    def test_toliq_ism(self):
        formatted_name = get_fullname('alijon', 'valiyev')
        self.assertEqual(formatted_name, 'Alijon Valiyev')
        
    def test_toliq_ism_otasi(self):
        name = get_fullname('hasan', 'husanov', 'olimovich')
        self.assertEqual(name, "Hasan Olimovich Husanov")
        
unittest.main()

