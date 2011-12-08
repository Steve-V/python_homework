#!/usr/bin/env python

#import 

def computeEx():
    ''' Compute e^x '''
    
    import math
    
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

def main():
    computeEx()
    
    
# Remember to unindent this line!
if __name__ == '__main__':
    main()