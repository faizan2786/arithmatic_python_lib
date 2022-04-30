import unittest
import math
from fp_arithmatic import *


class ArithmaticTestCases(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(add(10,20), 30)
    
    def test_multiplication(self):
        self.assertEqual(mul(4,5), 20)
    
    def test_dot(self):
        self.assertEqual(dot([1,2],[2,3]),8)
    
    def test_dot_float(self):
        self.assertAlmostEqual(dot([0.5,0.3],[1.2,0.25]), 0.675)

    def test_sqrt_1(self):
        self.assertEqual(sqrt(25), 5)
    
    def test_sqrt_2(self):
        self.assertAlmostEqual(sqrt(2), math.sqrt(2))
    
    def test_sqrt_3(self):
        self.assertEqual(sqrt(100), 10)
    
    def test_dist(self):
        self.assertEqual(distance([1,3],[4,7]), 5)
