#!/usr/bin/env python

#import 

def main():
  
  reverseString()
  swapVariables(5,1)
  isPrime()
  fibonacci()


def reverseString(someString = "Greeting"):
  '''Write a function to reverse a string provided by the user. Display the string before and after reversing. The default string value is “Greeting”.'''
  print("Old string: {}   New string: {}".format(someString,someString[::-1] ) )


def swapVariables(a,b):
  '''Write a function to swap two variables “a and b”. Variables can be int, string, list or dictionaries.'''
  return b,a


def isPrime():
  '''Return 1 if an argument is a prime number and 0 otherwise'''
  pass


def fibonacci():
  '''Write a recursive program to generate Fibonacci series for n numbers'''
  pass

  
if __name__ == '__main__':
  main()