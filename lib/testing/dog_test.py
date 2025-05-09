#!/usr/bin/env python3
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestDog:
    '''Dog in dog.py'''

    def test_is_class(self):
        '''is a class with the name "Dog"'''
       

class TestBark:
    '''Dog.bark() in dog.py'''

    def test_is_method(self):
        '''is an instance method'''
      
     

    def test_prints_woof(self):
        '''prints "Woof!"'''
        
     
        
        
        sys.stdout = sys.__stdout__
      

class TestSit:
    '''Dog.sit() in dog.py'''

    def test_is_method(self):
        '''is an instance method'''
     
        

    def test_prints_the_dog_is_sitting(self):
        '''prints "The dog is sitting."'''
        
        
      
        
        sys.stdout = sys.__stdout__
        
