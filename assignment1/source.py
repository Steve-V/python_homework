#!/usr/bin/env python

#import 

def main():

  Student = { "John" : { "join_date" : "05/03/2011", "Percent" : 80.055 }, "Don" : { "join_date" : "05/10/2011", "Percent" : 75.06777 }, "Smith" : { "join_date" : "04/04/2011", "Percent" : 85.8005 }}
  
  for name,namedata in Student.items():
    print(name)
    for eachitem,eachvalue in namedata.items():
      print(eachitem)
      print(eachvalue)
    

def fact():
  import math
  
  #get n
  n = float( input("Value of n: ") )
  
  #figure out the factorial using builtins
  mathFact = math.factorial(n)
  
  #figure out the factorial manually
  calcFact = math.sqrt(2 * math.pi * n) * math.pow((n / math.e),n)
  
  #output
  print("Approx  Factorial: %d \nCorrect Factorial: %d" % (calcFact,mathFact) )

if __name__ == '__main__':
  fact()

