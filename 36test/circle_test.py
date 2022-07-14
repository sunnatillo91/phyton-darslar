# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 19:13:54 2022

Dasturlash asoslari

#35-DARS. DASTURNI TEKSHIRISH  test

Author: Sunnatillo Xayrullayev 
"""

import unittest
from circle import getArea, getPerimeter

class CircleTest(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(getArea(10), 314.159)
        self.assertAlmostEqual(getArea(3), 28.27431)
    def test_perimeter(self):
        self.assertAlmostEqual(getPerimeter(10), 62.8318)
        self.assertAlmostEqual(getPerimeter(4), 25.13272)
        
unittest.main()
