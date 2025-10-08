#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 2024

@author: Charley Kirk
"""

from operator import itemgetter
import sys

current_county = None
county = None
current_cases = 0
current_deaths = 0
report_count = 0

#print("init")
for line in sys.stdin:
    line = line.strip()
    location, sdata = line.split('\t',1)
    county,date = location.split(',',1)
    scases, sdeaths = sdata.split(',',1)
    
    try:
        deaths = int(sdeaths)
        cases =  int(scases)
    except ValueError:
        #print ("valueerror")
        #exit
        continue
    
     # classic control break processing     
    if county==current_county:
        report_count+=1
    else:
        if current_county:
            print ("{}\t{} with {} deaths from {} daily reports".format(current_county, current_cases, current_deaths, report_count))
        current_cases=cases
        current_deaths=deaths
        current_county = county
        report_count=1
        continue

      
#print("end")
#if current_county == county:    
print ("{}\t{} with {} deaths from {} daily reports".format(county, current_cases, current_deaths, report_count))
        
    
