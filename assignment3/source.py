#!/usr/bin/env python

#import 

def main():
  
  #reverseString("5318008")
  #swapVariables(5,1)
  #print( isPrime( input("Enter a prime: ") ) )
  fibonacci()


def reverseString(someString = "Greeting"):
  '''Write a function to reverse a string provided by the user. Display the string before and after reversing. The default string value is “Greeting”.'''
  print("Old string: {}   New string: {}".format(someString,someString[::-1] ) )
  return someString[::-1]


def swapVariables(a,b):
  '''Write a function to swap two variables “a and b”. Variables can be int, string, list or dictionaries.'''
  return b,a


def isPrime(candidate):
  '''Return 1 if an argument is a prime number and 0 otherwise'''
  '''all primes are integers, that makes things nice'''
  #first, see if we can calculate this number at all
  
  # primes are only positive ints
  try:
    candidate = int(candidate)
  except ValueError:
    print("Input must be a positive integer!")
    return
  if candidate < 1:
    print("Input must be a positive integer!")
    return
  
  # see whether we've precalculated this prime
  if candidate < 10000000:
    from primes import primeset
    if candidate in primeset:
      return 1  # should be return True
    else:
      return 0  # should be return False
  
  # if not, we're going to be here for a while
  goAnyway = input("Warning!  This calculation may take a long time! Continue anyway? [y/N]: ")
  if goAnyway.lower() != 'y':
    return
  
  for i in range(10000000, candidate):
    if candidate % i == 0:
      return 0
  return 1

def fibonacci(n):
  '''Write a recursive program to generate Fibonacci series for n numbers'''
  if type(n) == int:
    # breakout criteria
    if n == 1:
      return [0]
    if n == 2:
      return [0,1]
    
    nextFib = fibonacci

  
if __name__ == '__main__':
  main()