"""
unittest/pytest (pip install pytest)
Unittest: Running a test: python -m unittest filename.py (-f argument optional to add if you want to stop the testing after the first error)
"""
import unittest

from test_func import area_of_square

import sys

class Testsomething(unittest.TestCase):
    def test_is_equal(self):
        #check if a==b
        self.assertEqual(10,10)


    def test_is_equal_fails(self):
        self.assertNotEqual(True, False)

    def test_not_equal(self):
        self.assertNotEqual("yellow", "blue")

    def test_is_in(self):
        self.assertIn(3, [7, 4, 5, 3, 2]) #if a is in be

    def test_is_upper(self):
        txt = "name".upper()
        self.assertEqual("NAME", txt)

    def test_area_of_square(self):
        len = 20
        area = area_of_square(len)
        self.assertEqual(area, len * len)



if __name__ == '__main__':
    unittest.main()

