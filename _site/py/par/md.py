#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
fp=open("README.md", "r");
for eachline in fp:
    #print eachline,;
    if ("-" in eachline[0] ):
        print eachline.lstrip(" - "),;
    elif ("## " in eachline)  :
        print "----"+eachline.lstrip("## "),;
    #print "==="+eachline+"===",;
