#!/usr/bin/env python

import csv

class ToolCsv:
    # Setup
    def __init__(self):
        
        # Does the file already exist?
        fileExists = True
        try:
            open('csv.db','rb')
        except:
            fileExists = False
        
        # If so, do nothing, otherwise, init
        if fileExists:
            return
        else:
            self.addTool("Hammer",76,11.99)
            self.addTool("Saw",88,12.00)
            self.addTool("Screwdriver",106,6.99)
            self.addTool("Wrench",34,7.50)
    
    def addTool(self, toolname, amount, price):
        '''Append a tool to the file'''
        writefile = open('csv.db','a')
        writeableLine = ','.join([toolname,str(amount),str(price)])
        writefile.write(writeableLine + '\n')
    
    def showAllTools(self):
        '''Output all the tools, in tabular format'''
        
        # This could be updated to detect terminal size
        width = 60
        columnsNeeded = 3
        
        #calculate max allowable width of any one column
        import math
        maxColumnWidth = math.floor( width / columnsNeeded)
        
        # Print header row
        headers = ['Tool Name','Quantity','Price']
        outputRow = ''
        for eachItem in headers:
            outputRow += "{k:^{maxColumnWidth}}".format(k=eachItem,maxColumnWidth=maxColumnWidth)
        print(outputRow)
        
        # Open the data file
        someFile = open('csv.db','r')
        fr = csv.reader(someFile)
        
        # Output the items in the file
        for eachLine in fr:
            outputRow = ""
            for eachItem in eachLine:
                outputRow += "{k:^{maxColumnWidth}}".format(k=eachItem,maxColumnWidth=maxColumnWidth)
            print(outputRow)
        someFile.close()
