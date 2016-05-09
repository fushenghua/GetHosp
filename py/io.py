#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
fp=open("io.txt", "r");
for eachline in fp:
    fobj = open("2016-05-03-"+eachline.rstrip()+".markdown", 'w')
    fobj.writelines("--- \n")
    fobj.writelines("layout: post \n")
    fobj.writelines("title: "+eachline+"\n")
    fobj.writelines("date:   2016-05-03 13:39:56 \n")
    fobj.writelines("categories: hosp \n")
    fobj.writelines("--- \n")
    fobj.writelines("   \n")
    fobj.writelines(eachline)
    fobj.close()
    print eachline,;

def print_func( par ):
   print "Hello : ", par
   return
