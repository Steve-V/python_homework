#!/usr/bin/env python

import sqlite3

def sumall(tab):
    pass

def main():
    db_conn = sqlite3.connect("sq.db")
    db_curr = db_conn.cursor()
    
    db_curr.execute( "SELECT * FROM numers;")
    db_result = db_curr.fetchall()
    
    for eachrow in db_result:
        print (eachrow[-1])
    
    
# Remember to unindent this line!
if __name__ == '__main__':
    main()