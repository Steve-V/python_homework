#!/usr/bin/env python

def main():
  fact()
  table()
  
def table():
  '''Draw tabular student data'''
  
  #determine if the program should autodetect terminal width
  useExternalCode = askExternalCode()
  
  #define the data table
  Student = { "John" : { "join_date" : "05/03/2011", "Percent" : 80.055}, "Don" : { "join_date" : "05/10/2011", "Percent" : 75.06777}, "Smith" : { "join_date" : "04/04/2011", "Percent" : 85.8005}}
  
  #convert the integers to percentage strings
  fixIntegers(Student)
  
  #create a set to store the various student data headers
  headerset = set([])
  
  #step through the data table, discover the headers, and put them in the set
  for namedata in Student.values():
    for eachitem in namedata.keys():
      headerset.add(eachitem)
  
  #add the word "student" to the list of headers
  headers = ["Student"]
  
  #extend the rest of the headers into the list
  headers.extend( list(headerset) )
  
  #discover the terminal width
  width = getTerminalWidth(useExternalCode)
  
  #discover the amount of columns needed
  columnsNeeded = len(headers)
  
  #calculate max allowable width of any one column
  import math
  maxColumnWidth = math.floor( width / columnsNeeded)
  
  #print top dotted line
  dottedLine = '-' * width
  print(dottedLine)
  
  #create header row
  outputRow = "|".join( "{k:^{maxColumnWidth}}".format(k=k,maxColumnWidth=maxColumnWidth) for k in headers )
  
  #add leading and trailing pipe characters
  outputRow = addPipes(outputRow)
  
  #output header
  print(outputRow)
  
  #create empty header row
  emptyHeaders = [""]*columnsNeeded
  outputRow = "|".join( "{k:^{maxColumnWidth}}".format(k=k,maxColumnWidth=maxColumnWidth) for k in emptyHeaders )
  
  #output empty header row and separator
  print( addPipes(outputRow) )
  print(dottedLine)
  
  #step through the data table, build the output string for each student, and output it
  
  for name,namedata in Student.items():
    #get the student name
    outputRow = "{name:^{maxColumnWidth}}".format(name=name,maxColumnWidth=maxColumnWidth)
    
    #get the rest of the student data
    outputData = "|".join( "{k:^{maxColumnWidth}}".format(k=namedata[eachHeader],maxColumnWidth=maxColumnWidth) for eachHeader in headerset )
    
    #combine the two items and add a pipe separator
    outputRow = outputRow + "|" + outputData
    
    #add the borders and print
    print( addPipes(outputRow) )
    
    #finally, draw another dotted line separator
    print(dottedLine)

def addPipes(datastring):
  '''Add bordering pipe characters to a line'''
  newData = list(datastring)
  newData[0] = "|"
  newData[-1] = "|"
  return "".join(newData)

def fixIntegers(Student):
  '''Round floating point numbers and add % symbol'''
  import decimal
  for name, namedata in Student.items():
    for k,v in namedata.items():
      if type(v) == float:
        namedata[k] = str(decimal.Decimal(str(v)).quantize(decimal.Decimal('.01'), rounding="ROUND_DOWN") ) + "%"
  return Student

def fact():
  '''Calculate factorial of a given number'''
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

def askExternalCode():
  shouldUseExternalCode = input("Autodetect Terminal Width? (y/N): ")
  try:
    if shouldUseExternalCode.lower() == 'y':
      return True
  except:
    pass
  return False

def getTerminalWidth(useExternalCode):
  '''Discover the current width of the terminal window'''
  if useExternalCode:
    try:
      from getTerminalSize import getTerminalSize
    except ImportError:
      print("\nCan't find getTerminalSize.py in current folder! \nUsing default terminal size...")
      return 70
    try:
      #don't go all the way to the edge
      width = getTerminalSize()[0] - 2
    except TypeError:
      print("Can't detect terminal width in this environment!\nUsing default terminal size...")
      return 70
    #if everything worked fine, then...
    return width
  else:
    #use default value
    return 70

if __name__ == '__main__':
  main()

