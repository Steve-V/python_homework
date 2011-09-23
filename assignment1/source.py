#!/usr/bin/env python

def main():
  #fact()
  table()
  
def table():
  
  debug = True
  
  #define the data table
  Student = { "John" : { "join_date" : "05/03/2011", "Percent" : 80.055 }, "Don" : { "join_date" : "05/10/2011", "Percent" : 75.06777 }, "Smith" : { "join_date" : "04/04/2011", "Percent" : 85.8005 }}
  
  #create a set to store the various student data headers
  headerset = set([])
  
  #step through the data table
  #discover the headers
  #and put them in the set
  for namedata in Student.values():
    for eachitem in namedata.keys():
      headerset.add(eachitem)
  
  #add student to the list of headers
  headers = ["Student"]
  if debug: print("Headers before extend: %s" % headers)
  
  #extend the rest of the headers into the list
  headers.extend( list(headerset) )
  if debug: print("Headers after extend: %s" % headers)
  
  #discover the terminal width
  width = getTerminalWidth()
  if debug: print("Current Terminal Width: %d" % width)
  
  #discover the amount of columns needed
  columnsNeeded = len(headers)
  if debug: print("Columns needed: %d" % columnsNeeded)
  
  #calculate max width of any one column
  import math
  maxColumnWidth = math.floor( width / columnsNeeded)
  if debug: print("Max column width: %d" % maxColumnWidth)
  
  #print top dotted line
  dottedLine = '-' * width
  print(dottedLine)
  
  #create and print header row
  print(headers)
  #headerRow = "|".join( ["%s" % k.center(maxColumnWidth) for k in headers] )
  headerRow = "|".join( "{k:^{maxColumnWidth}}".format(k=k,maxColumnWidth=maxColumnWidth) for k in headers )

  #headerRow[0] = "|"
  #headerRow[-1] = "|"
  print(headerRow)

  #print("|" + eachname.center( int(maxColumnWidth - 2) )[: int(maxColumnWidth - 2 ) ] + "|")
  
  #print each student, including bottom separator
  
  
  
  
  #for name,namedata in Student.items():
    #print(name)
    #print(namedata)
    

def fact():
  import math
  
  #get n, make sure it is a number
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


def getTerminalWidth():
  #placeholder
  return 70

if __name__ == '__main__':
  main()

