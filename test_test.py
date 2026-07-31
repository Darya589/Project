import unittest
from test import summa, r

class test(unittest.TestCase):

    def test_summa(self):
        self.assertEqual(summa(2, 5), 7)
        self.assertEqual(summa(-1, -5), -6)

    def test_r(self):
        self.assertEqual(r(10, 2), 5.00)
        self.assertEqual(r(15, 5), 3.00)
        self.assertEqual(r(1, 3), 0.33)
       
