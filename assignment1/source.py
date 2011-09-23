#!/usr/bin/env python

def main():
  #fact()
  table()
  
def table():
  
  debug = True
  
  #define the data table
  Student = { "John" : { "join_date" : "05/03/2011", "Percent" : 80.055 }, "Don" : { "join_date" : "05/10/2011", "Percent" : 75.06777 }, "Smith" : { "join_date" : "04/04/2011", "Percent" : 85.8005 }}
  
  #create a set to store the various student data headers
  headers = set([])
  
  #step through the data table
  #discover the headers
  #and put them in the set
  for namedata in Student.values():
    for eachitem in namedata.keys():
      if debug: print(eachitem)
      headers.add(eachitem)
  
  
  #for name,namedata in Student.items():
    #print(name)
    #print(namedata)
    

def fact():
  import math
  
  #get n
  try:
    n = float( input("Value of n: ") )
  except ValueError:
    print("Error: n must be a number!")
    return
  
  #figure out the factorial using builtins
  mathFact = math.factorial(n)
  
  #figure out the factorial manually
  calcFact = math.sqrt(2 * math.pi * n) * math.pow((n / math.e),n)
  
  #output
  print("Approx  Factorial: %d \nCorrect Factorial: %d" % (calcFact,mathFact) )

if __name__ == '__main__':
  main()

