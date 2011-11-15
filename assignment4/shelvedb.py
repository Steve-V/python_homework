#!/usr/bin/env python

import shelve


class ToolShelf:
    # Setup
    def __init__(self):
        self.addTool("Hammer",76,11.99)
        self.addTool("Saw",88,12.00)
        self.addTool("Screwdriver",106,6.99)
        self.addTool("Wrench",34,7.50)
    
    def addTool(self, toolnameIn, amountIn, priceIn):
        self.db = shelve.open("shelve.db")
        self.db[ str(toolnameIn) ] = {"toolname":toolnameIn, "amount":amountIn, "price":priceIn}
        self.db.close()
        return
    
    def getToolData(self, toolname):
        self.db = shelve.open("shelve.db")
        try:
            data = self.db[toolname]
        except KeyError:
            return None
        self.db.close()
        return data
    
    def getAllTools(self):
        self.db = shelve.open("shelve.db")
        returnDict = {}
        for eachKey in self.db.keys():
            returnDict[ eachKey ] = self.db[eachKey]
        self.db.close()
        return returnDict


#def main():
    
    #pass
    
    
#if __name__ == '__main__':
    #main()
