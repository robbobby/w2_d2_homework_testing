import unittest
from src.calculator import *

class TestCalculator(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(7, add(3 , 4))

    def test_divide(self):
        self.assertEqual(3, divide(9, 3))

    def test_subtract(self):
        self.assertEqual(4, subtract(7, 3))
    
    def test_multiply(self):
        self.assertEqual(9, multiply(3, 3))