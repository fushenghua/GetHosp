#!/usr/bin/python
# -*- coding: UTF-8 -*-
def print_func( par ):
   print "Hello : ", par
   return

def hello():
    print "hello world"
    for str in "hello world":
        sayHi(str)
        sayHi(str=str)

def sayHi(str):
    print str

hello()
