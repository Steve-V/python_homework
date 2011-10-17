#!/usr/bin/env python

#import 

def main():
  
  #howMany = int( input("Max Prime: ") )
  
  howMany = 10000000
  
  print( rwh_primes(howMany) )
  
def rwh_primes(n):
  # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
  """ Returns  a list of primes < n """
  sieve = [True] * n
  for i in xrange(3,int(n**0.5)+1,2):
      if sieve[i]:
          sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
  return [2] + [i for i in xrange(3,n,2) if sieve[i]]

  
  
if __name__ == '__main__':
  main()