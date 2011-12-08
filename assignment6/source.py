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
    '''See if the database file exists'''
    try:
        open("tools.db")
    except:
        return False
    else:
        return True

def createDatabase():
    '''Connect to and initialize the database'''
    
    db_conn = sqlite3.connect("tools.db")
    db_curr = db_conn.cursor()

    db_curr.execute( "CREATE TABLE 'inventory' ('toolName' TEXT PRIMARY KEY, 'quantity' INTEGER, 'cost' REAL);" )
    db_curr.execute( "INSERT INTO 'inventory' VALUES ('Hammer','76','11.99');" )
    db_curr.execute( "INSERT INTO 'inventory' VALUES ('Saw','88','12.00');" )
    db_curr.execute( "INSERT INTO 'inventory' VALUES ('Screwdriver','106','6.99');" )
    db_curr.execute( "INSERT INTO 'inventory' VALUES ('Wrench','34','7.50');" )
    
    db_conn.commit()

def getCommand(whatType):
    '''Find out what the user wants us to do'''
    
    # Set up the question
    ask = "(1) - Add new tool\n(2) - Tool Lookup\n(3) - Update Tool\n(4) - Exit\nCommand: "
    valid = ['1','2','3']
    
    # Talk to the user
    command = input(ask)
    
    # Validity check
    if command.strip() not in valid:
        return None
    return command
    
def hardware():
    ''' Run hardware store database '''
    
    if firstRun():
        createDatabase()
    
    again = True
    while again:
        command = getCommand()
        
        if command == "1":
            addNewTool()
        elif command == "2":
            showTool()
        elif command == "3":
            changeTool()
        else:
            again = False
     

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