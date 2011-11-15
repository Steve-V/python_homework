#!/usr/bin/env python

import csv


class ToolCsv:
    # Setup
    def __init__(self):
        self.addTool("Hammer",76,11.99)
        self.addTool("Saw",88,12.00)
        self.addTool("Screwdriver",106,6.99)
        self.addTool("Wrench",34,7.50)
    
    def addTool(self, toolname, amount, price):
        self.db = csvwriter.open("csv.db")
        self.db.writeline([toolname, amount, price])
        self.db.close()
    
    def showAllTools(self):
        self.db = csvreader.open("csv.db")
        for eachLine in self.db.readlines():
            for eachItem in eachLine:
                print("{k:^{maxColumnWidth}}".format(k=eachItem,maxColumnWidth=maxColumnWidth) ) )
        self.db.close()
        return returnDict
