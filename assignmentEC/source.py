#!/usr/bin/env python

import math

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
    

def main():
    #computeEx()
    hanoi()
    
# Remember to unindent this line!
if __name__ == '__main__':
    main()