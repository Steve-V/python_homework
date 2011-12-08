#!/usr/bin/env python

#import 

def main():
    '''Draw a barchart with matplotlib'''
    import numpy as np
    import matplotlib.pyplot as plt


    N = 3
    adults   = (300, 500, 700)
    kids = (200,600,600)
    ind = np.arange(N)
    width = 0.35

    p1 = plt.bar(ind, adults,   width, color='r')
    p2 = plt.bar(ind+width, kids, width, color='b')

    plt.ylabel('Visitors')
    plt.title('Visitors by month')
    plt.xticks(ind+width/2., ('April', 'May', 'June') )
    plt.yticks(np.arange(0,1000,100))
    plt.legend( (p1[0], p2[0]), ('Adults', 'Kids') )

    plt.show()

    
#Remember to unindent this line!
if __name__ == '__main__':
    main()