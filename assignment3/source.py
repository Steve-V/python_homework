#!/usr/bin/env python

#import 

def main():
  
  reverseString( input("String to reverse: " ) )
  print( "Reversing ('A','B'): {}".format( swapVariables("A","B") ) )
  print( isPrime( input("Enter a prime: ") ) )
  print( fibonacci( input("Fibonacci sequence length: ") ) )


def reverseString(someString):
  '''Write a function to reverse a string provided by the user. Display the string before and after reversing. The default string value is “Greeting”.'''
  if not someString:
    someString = "Greeting"
  print("Old string: {}   New string: {}".format(someString,someString[::-1] ) )
  return someString[::-1]


def swapVariables(a,b):
  '''Write a function to swap two variables “a and b”. Variables can be int, string, list or dictionaries.'''
  return b,a


def isPrime(candidate):
  '''Return 1 if an argument is a prime number and 0 otherwise
  This is not the "correct" thing to do - in Python you should be returning True and False rather than 1 and 0, oh well'''
  
  # primes are only positive ints
  try:
    candidate = int(candidate)
  except ValueError:
    return("Input must be a positive integer!")
  if candidate < 1:
    return("Input must be a positive integer!")
  
  # see whether we've precalculated this prime
  if candidate < 10000000:
    try:
      from primes import primeset
      if candidate in primeset:
        return 1  # should be return True
      else:
        return 0  # should be return False
    except ImportError:
      pass
    
  # if not, we're going to be here for a while
  goAnyway = input("Warning!  This calculation may take a long time!\nContinue anyway? [y/N]: ")
  if goAnyway.lower() != 'y':
    return("Calculation aborted")
  
  for i in range(3, candidate):
    if candidate % i == 0:
      return 0
  return 1

def fibonacci(n):
  '''Write a recursive program to generate Fibonacci series for n numbers'''
  
  # cast to int
  try:
    n = int(n)
  except ValueError:
    return("Input must be a positive integer!")
  
  # breakout criteria
  if n == 0:
    return("Empty list!")
  if n == 1:  
    return [0]
  if n == 2:
    return [0,1]
  
  # get next lower fibonacci sequence and add
  fibList = fibonacci(n-1)
  fibList.append( fibList[-1] + fibList[-2] )
  
  return fibList

  
if __name__ == '__main__':
  main()