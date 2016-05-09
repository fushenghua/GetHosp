#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
<<<<<<< HEAD
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
=======


def createMDForFile():
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

def createMD(title,cate,city,info):
        fobj = open("../_posts/2016-05-03-"+title.rstrip()+".markdown", 'w')
        fobj.writelines("--- \n")
        fobj.writelines("layout: post \n")
        fobj.writelines("title: "+title+"\n")
        fobj.writelines("date:   2016-05-03 13:39:56 \n")
        fobj.writelines("categories: "+cate+"  \n")
        fobj.writelines("city: "+city+"  \n")
        fobj.writelines("--- \n")
        fobj.writelines("   \n")
        fobj.writelines(title+"\n")
        fobj.writelines(info+"\n")
        fobj.close()
>>>>>>> c3d08767bfcf9d674b09ab1d9e9618b2c8a90ab0
