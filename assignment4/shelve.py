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
        db = shelve.open("shelve.db")
        db[ str(toolnameIn) ] = {"toolname":toolnameIn, "amount":amountIn, "price":priceIn}
        db.close()
        return
    
    def getToolData(self, toolname):
        db = shelve.open("shelve.db")
        return db[toolname]
        db.close()
    
    def getAllTools(self):
        db = shelve.open("shelve.db")
        returnDict = {}
        for eachKey in db.keys():
            returnDict[ db[toolname] ] = {"toolname":db[toolname], "amount":db[amount], "price":db[price]}
        db.close()
        return returnDict


#def main():
    
    #pass
    
    
#if __name__ == '__main__':
    #main()
