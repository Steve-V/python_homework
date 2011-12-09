#!/usr/bin/env python

import math

def getBS():
    import random
    return("BS" + str(random.choice( range(1,999) ) ) )

def computeEx():
    ''' Compute e^x '''
    
    try:
        xval = int(input("X value: ") )
        nval = int(input("N value: ") )
    except ValueError:
        print("Error!")
        return
    
    total = 1
    
    for n in range(1,nval):
        total += ( math.pow(xval,n) / math.factorial(n) )
    
    print( "Estimate: {}".format(total) )
    print( "Actual: {}".format(math.exp(xval) ) )

def hanoi():
    ''' Play the Towers of Hanoi '''
    def moveHanoi(num, start, end, temp):
        if num == 1:
            print("Move the plate from {} to {}".format(start, end) )
        else:
            moveHanoi(num-1, start, temp, end)
            moveHanoi(1, start, end, temp)
            moveHanoi(num-1, temp, end, start)
    
    try:
        totalDiscs = int(input("How many discs: ") )
    except ValueError:
        print("Need an integer!")
    
    moveHanoi(totalDiscs, "A", "C", "B")
    
    print("Total number of moves: {}".format( int( math.pow(2,totalDiscs) - 1 ) ) )
    

def dbase():
    ''' Do some database operations '''
    import sqlite3
    
    def firstRun():
        '''See if the database file exists'''
        # Cause an error if the file doesn't exist
        try:
            db_conn = sqlite3.connect("univ.db")
            db_curr = db_conn.cursor()
            db_curr.execute( "SELECT * FROM students;" )
            db_result = db_curr.fetchall()
        
        # An error occurred, this is the first run
        except:
            return True
        # No error occurred, this is not the first run
        else:
            return False

    def createDatabase():
        '''Connect to and initialize the database'''
        
        db_conn = sqlite3.connect("univ.db")
        db_curr = db_conn.cursor()

        db_curr.execute( "CREATE TABLE 'students' ('win' TEXT PRIMARY KEY, 'firstname' TEXT, 'lastname' TEXT);" )
        
        db_curr.execute( "CREATE TABLE 'courses' ('coursenum' TEXT PRIMARY KEY, 'description' TEXT);" )
        
        db_curr.execute( "CREATE TABLE 'enrolled' ('id' INTEGER PRIMARY KEY AUTOINCREMENT, 'win' TEXT, 'coursenum' TEXT);" )
        
        db_conn.commit()
    
    def populateDatabase():
        ''' Populate the database with the initial values '''
        
        # Open the database
        db_conn = sqlite3.connect("univ.db")
        db_curr = db_conn.cursor()
        
        # Open the textfile
        textfile = open("textfile.txt",'r')
        
        # Read the text file into the database
        for lines in textfile.readlines():
            eachline = lines.split(":")
            win = eachline[0]
            firstname = eachline[1]
            lastname = eachline[2]
            courses = eachline[3:]
            
            # Get rid of the newlines
            courses.append( courses.pop().strip() )
            
            db_curr.execute( "INSERT INTO 'students' VALUES (?,?,?);", (win, firstname, lastname)  )
            
            for eachcourse in courses:
                try:
                    db_curr.execute( "INSERT INTO 'courses' VALUES (?,?);", (eachcourse, getBS() ) )
                except sqlite3.IntegrityError:
                    pass
                db_curr.execute( "INSERT INTO 'enrolled' VALUES (?,?,?);", (None, win, eachcourse) )
        
        db_conn.commit()

    if firstRun():
        createDatabase()
        populateDatabase()

    








def main():
    #computeEx()
    #hanoi()
    dbase()
    
# Remember to unindent this line!
if __name__ == '__main__':
    main()