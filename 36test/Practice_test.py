# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 12:05:24 2022

#35-DARS. DASTURNI TEKSHIRISH  practice test

Author: Sunnatillo Xayrullayev
"""

# 1
# import unittest
# from Practice import sonKattami, sonJuftmi

# class sonKattamiTest(unittest.TestCase):
#     def test_true(self):
#         self.assertGreater(sonKattami(7, 5, 3)
        
# # unittest.main()



# 3
import unittest

from Practice import sonJuftmi

class sonJuftmiTest(unittest.TestCase):
    def test_true(self):
        self.assertTrue(sonJuftmi(34))
        self.assertTrue(sonJuftmi(56))
        self.assertTrue(sonJuftmi(348))
    def test_false(self):
        self.assertFalse(sonJuftmi(45))
        self.assertFalse(sonJuftmi(455))
        self.assertFalse(sonJuftmi(245))
        
unittest.main()
    

