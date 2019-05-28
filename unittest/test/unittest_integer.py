#! /usr/local/bin/python3

#libraries needed
import os, sys
import unittest



#my files to test
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import basicfile

#insert path: 
#path of current file:  os.path.abspath(__file__)
#path of current dir(up one level):   os.path.dirname(os.path.abspath(__file__))
#path of one dir up:    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#insert before the element 0 of the list(of path) the directory one level up
#remember to put before inserting the module you test




class MyTests(unittest.TestCase):

#    def test_type_a(self):
#        a = 'z'
#        self.assertTrue(type(a) == int)
#        #self.assertTrue(type(basicfile.uselessmath(a,b)) == int) 
#    
#    def test_type_b(self):
#        b = 4
#        self.assertTrue(type(b) == int)
#        #self.assertTrue(type(basicfile.uselessmath(a,b)) == int) 

    def test_type(self):
        for i in range(0,20):
            with self.subTest( num = i):
                self.assertEqual(type(i), int)
    
    def test_library(self):
        a = basicfile.uselessmath(5,5)
        self.assertEqual(type(a), int)


if __name__ == "__main__":
    unittest.main()