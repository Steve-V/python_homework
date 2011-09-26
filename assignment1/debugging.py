#!/usr/bin/env python

def main():
  fact()
  table()
  
def table():
  
  debug = False
  useExternalCode = True
  
  #define the data table
  Student = { "John" : { "join_date" : "05/03/2011", "Percent" : 80.055}, "Don" : { "join_date" : "05/10/2011", "Percent" : 75.06777}, "Smith" : { "join_date" : "04/04/2011", "Percent" : 85.8005}}
  
  #Student = { "John" : { "join_date" : "05/03/2011", "Percent" : 80.055, "hottness":"low","confidence":"low"}, "Don" : { "join_date" : "05/10/2011", "Percent" : 75.06777 , "hottness":"low","confidence":"high"}, "Smith" : { "join_date" : "04/04/2011", "Percent" : 85.8005, "hottness":"high","confidence":"moderate" }}
  
  #convert the integers to percentage strings
  fixIntegers(Student)
  
  #create a set to store the various student data headers
  headerset = set([])
  
  #step through the data table
  #discover the headers
  #and put them in the set
  for namedata in Student.values():
    for eachitem in namedata.keys():
      headerset.add(eachitem)
  
  #add the word "student" to the list of headers
  headers = ["Student"]
  if debug: print("Headers before extend: %s" % headers)
  
  #extend the rest of the headers into the list
  headers.extend( list(headerset) )
  if debug: print("Headers after extend: %s" % headers)
  
  #discover the terminal width
  width = getTerminalWidth(useExternalCode)
  if debug: print("Current Terminal Width: %d" % width)
  
  #discover the amount of columns needed
  columnsNeeded = len(headers)
  if debug: print("Columns needed: %d" % columnsNeeded)
  
  #calculate max allowable width of any one column
  import math
  maxColumnWidth = math.floor( width / columnsNeeded)
  if debug: print("Max column width: %d" % maxColumnWidth)
  
  #print top dotted line
  dottedLine = '-' * width
  print(dottedLine)
  
  #create header row
  if debug: print(headers)
  outputRow = "|".join( "{k:^{maxColumnWidth}}".format(k=k,maxColumnWidth=maxColumnWidth) for k in headers )
  
  #add leading and trailing pipe characters
  outputRow = addPipes(outputRow)
  
  #output header
  print(outputRow)
  
  #create empty header row
  emptyHeaders = [""]*columnsNeeded
  if debug: print(emptyHeaders)
  outputRow = "|".join( "{k:^{maxColumnWidth}}".format(k=k,maxColumnWidth=maxColumnWidth) for k in emptyHeaders )
  
  #output empty header row and separator
  print( addPipes(outputRow) )
  print(dottedLine)
  
  #step through the data table, build the output string for each student, and output it
  
  for name,namedata in Student.items():
    outputRow = "{name:^{maxColumnWidth}}".format(name=name,maxColumnWidth=maxColumnWidth)
    if debug: print("Name output: %s \nName Data: %s" % (outputRow, namedata))
    
    outputData = "|".join( "{k:^{maxColumnWidth}}".format(k=namedata[eachHeader],maxColumnWidth=maxColumnWidth) for eachHeader in headerset )
    
    if debug: print("Output Data String: %s" % outputData)
    
    #combine the two items and add a pipe separator
    outputRow = outputRow + "|" + outputData
    
    if debug: print("Pre-Pipe output row: %s" % outputRow)
    
    #add the borders and print
    print( addPipes(outputRow) )
    
    #finally, draw another dotted line separator
    print(dottedLine)

def addPipes(datastring):
  newData = list(datastring)
  newData[0] = "|"
  newData[-1] = "|"
  return "".join(newData)

def fixIntegers(Student):
  import decimal
  for name, namedata in Student.items():
    for k,v in namedata.items():
      if type(v) == float:
        namedata[k] = str(decimal.Decimal.from_float(v).quantize(decimal.Decimal('.01'), rounding="ROUND_DOWN") ) + "%"
  return Student

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


def getTerminalWidth(useExternalCode):
  if useExternalCode:
    from getTerminalSize import getTerminalSize
    width = getTerminalSize()[0] - 2
    return width
  else:
    #use default value
    return 70

if __name__ == '__main__':
  main()

