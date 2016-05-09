#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import sys
import pu
# from io import *

fp=open("README.md", "r");
for eachline in fp:
    print eachline,;
    if ("-" in eachline[0] ):
        print eachline.lstrip(" - "),;
    elif ("## " in eachline)  :
        print "----"+eachline.lstrip("## "),;
    # pu.print_func('Zara');
    # io.print_func("Hello ");
    # io.print_func("Hello")
    #print "==="+eachline+"===",;
