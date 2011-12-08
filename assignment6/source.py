#!/usr/bin/env python

import sqlite3


def problemData():
    '''
    Tool name
        Hammer
        Saw
        Screwdriver
        Wrench
    Quantity
        76
        88
        106
        34
    Cost
        11.99
        12.00
        6.99
        7.50
    '''
    pass

def firstRun():
    try:
        open("tgg.db")
    except:
        return False
    else:
        return True

def showMenu():
    print("MENU.  What do?!!")
    
def hardware():
    ''' Run hardware store database '''
    
    if firstRun():
        createDatabase()
    
    again = True
    while again:
        command = showMenu()
        
        if command == "addTool":
            addNewTool()
        elif command == "showTool":
            showTool()
        elif command == "changeTool":
            changeTool()
        else:
            again = False
     
     
    pass

def barchart():
    '''
     Using matplotlib for Python, draw a barchart for the following information
        Month
            April
            May
            June
        Number of Visitors(Adult)
            300
            500
            700
        Number of Visitors(Children)
            200
            600
            600
    '''
    
    pass




def main():
    hardware()
    #barchart()
    
    
# Remember to unindent this line!
if __name__ == '__main__':
    main()