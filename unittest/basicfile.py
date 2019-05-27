#! /usr/local/bin/python3

import sys, os



def uselessmath(a,b):
    c = a + b 
    return c




#main function
def main (a,b):
    uselessmath(a,b)




if __name__ == "__main__":
    
    first = int(sys.argv[1])
    second = int(sys.argv[2])

    main( first , second )

