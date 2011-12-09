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
    
    def getCommand():
        '''Find out what the user wants us to do'''
        
        # Set up the question
        ask = "(1) - Show all WINs\n(2) - Show Detail\n(3) - Exit\nCommand: "
        valid = ['1','2']
        
        # Talk to the user
        command = input(ask)
        
        # Validity check
        if command.strip() not in valid:
            return None
        return command
    
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
    
    def showWins():
        ''' Show all win numbers in the database '''
        
        # Open the database
        db_conn = sqlite3.connect("univ.db")
        db_curr = db_conn.cursor()
        db_curr.execute( "SELECT win FROM students;" )
        db_result = db_curr.fetchall()

        if (db_result):
            print("Available WIN Numbers: \n")
            for eachrow in db_result:
                print(eachrow[0])
            print('\n')
    
    def showDetail():
        ''' Get Detail about a particular WIN '''
        
        # Open the database
        db_conn = sqlite3.connect("univ.db")
        db_curr = db_conn.cursor()
        
        # Figure out who we want
        request = input("WIN: ")
        
        # Get their personal info
        for person in db_curr.execute( "SELECT firstname,lastname FROM students WHERE win = ?;", (request,) ):
            print("First Name: {}\nLast Name: {}\nEnrolled in:".format(person[0],person[1]) )
        
        # Get which courses they are in
        
        db_curr.execute( "SELECT coursenum FROM enrolled WHERE win = ?;", (request,) )
        
        coursesEnrolled = db_curr.fetchall()
        
        for eachitem in coursesEnrolled:
            #print(eachitem[0])
            print("   " + db_curr.execute( "SELECT description FROM courses WHERE coursenum = ?;", (eachitem[0],) ).fetchone()[0] )
        
        print('')
    # ======================================
    
    if firstRun():
        createDatabase()
        populateDatabase()
    
    again = True
    while again:
        command = getCommand()
        
        if command == "1":
            showWins()
        elif command == "2":
            showDetail()
        else:
            again = False


def main():
    computeEx()
    hanoi()
    dbase()
    
# Remember to unindent this line!
if __name__ == '__main__':
    main()