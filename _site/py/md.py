#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import io

city=""
hospname="";
info="信息\n";
cate="其他"
i=0;

fp=open("README.md", "r");
for eachline in fp:
    #print eachline,;
    if ("- " == eachline[0:2] ):
        if (hospname!=eachline and hospname != ""):

            print "create "+hospname
            i=i+1
            print i
            io.createMD(hospname,cate,city,info)
            info="信息\n";
            cate="其他"

        hospname = eachline.lstrip(" - ").replace("/","、");


    elif (" - " == eachline[0:3] ):
        info = info + eachline+"\n";
    elif ("## " == eachline[0:3]):
        city=eachline.lstrip("## ");
    elif ("### " == eachline[0:4]):
        cate=eachline.lstrip("### ");
