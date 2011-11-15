#!/usr/bin/env python

import unittest

class outOfRangeException(Exception):
    pass

class NANException(Exception):
    pass

class Rectangle:
    # Setup
    def __init__(self,length=1.0,width=1.0):
        self.setLength(length)
        self.setWidth(width)
    
    # Get and set
    def setLength(self, new):
        self.__length = new
    def setWidth(self, new):
        self.__width = new
    def getLength(self):
        return self.__length
    def getWidth(self):
        return self.__width
    
    # Calculations
    def perimeter(self):
        return (2*self.__length) + (2*self.__width)
    def area(self):
        return self.__length * self.__width
    

class TestRectangle(unittest.TestCase):
    # Build a rectangle that can be used for the tests
    def setUp(self):
        self.r = Rectangle(2,5)
    
    def test_checkPerimeter(self):
        '''Checking perimeter of rectangle'''
        self.assertEqual(self.r.perimeter(), 14)
    
    def test_checkArea(self):
        '''Checking area of rectangle'''
        self.assertEqual(self.r.area(), 10)
    
    
def main():
    unittest.main()
    
    
    
# Remember to unindent this line!
if __name__ == '__main__':
    main()