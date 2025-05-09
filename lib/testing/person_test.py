#!/usr/bin/env python3

from person import Person

import io

import types

class TestPerson:
    '''Person in person.py'''

    def test_is_class(self):
        '''is a class with the name "Person"'''
        guido = Person()
        

class TestTalk:
    '''Person.talk() in person.py'''

    def test_is_method(self):
        '''is an instance method'''
        guido = Person()
        assert(type(guido.talk) == types.MethodType)

    def test_prints_hello_world(self):
        '''prints "Hello World!"'''
        guido = Person()
        captured_out = io.StringIO()
        
        guido.talk()
      
        

class TestWalk:
    '''Person.walk() in walk.py'''

    def test_is_method(self):
        '''is an instance method'''
        guido = Person()
        assert(type(guido.walk) == types.MethodType)

    def test_prints_the_person_is_walking(self):
        '''prints "The person is walking."'''
        guido = Person()
        captured_out = io.StringIO()
        
        guido.walk()
      
        
