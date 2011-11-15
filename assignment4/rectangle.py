#!/usr/bin/env python

import unittest

class outOfRangeException(Exception):
    pass

class NanException(Exception):
    pass

class Rectangle:
    # Setup
    def __init__(self,length=1.0,width=1.0):
        # We use the setters so we get error checking for free
        self.setLength(length)
        self.setWidth(width)
    
    def checkValue(self, new):
        # This way we don't have to have the same code in multiple places
        try:
            float(new)
        except ValueError:
            raise NanException
        if new <= 0 or new >= 20:
            raise outOfRangeException
        else:
            return new
    
    # Get and set
    def setLength(self, new):
        self.__length = self.checkValue(new)
    def setWidth(self, new):
        self.__width = self.checkValue(new)
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
    
    def test_checkOutOfBoundsValue_high(self):
        '''Checking out of bounds value trap - high'''
        self.assertRaises(outOfRangeException, self.r.setLength, 30)
    
    def test_checkOutOfBoundsValue_low(self):
        '''Checking out of bounds value trap - low'''
        self.assertRaises(outOfRangeException, self.r.setLength, -3)
    
    def test_checkNanException(self):
        '''Checking if an exception is thrown when input is not a number'''
        self.assertRaises(NanException, self.r.setLength, "farts")
    
def main():
    unittest.main()
    
    
    
# Remember to unindent this line!
if __name__ == '__main__':
    main()