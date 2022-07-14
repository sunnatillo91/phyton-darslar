# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 08:33:50 2022

#35-DARS. DASTURNI TEKSHIRISH  tubSon test

Author: Sunnatillo Xayrullayev
"""

import unittest
from tubSonmi import tubSonmi

class tubSonTest(unittest.TestCase):
    def test_true(self):
        self.assertTrue(tubSonmi(5))
        self.assertTrue(tubSonmi(193))
        self.assertTrue(tubSonmi(547))
    def test_false(self):
        self.assertFalse(tubSonmi(7))
        self.assertFalse(tubSonmi(19))
        self.assertFalse(tubSonmi(9))

unittest.main()        
        