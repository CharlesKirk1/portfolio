#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 2024

@author: Charley Kirk
"""

import sys
from datetime import date
from datetime import timedelta

today = date.today().toordinal()
#print(today)
header = True
for line in sys.stdin:
    if header :
        header = False
    else:
        line = line.strip()
        datadate,county,state,fips,cases,deaths= line.split(',')
        if state=="Pennsylvania":
            delta = today - date.fromisoformat(datadate).toordinal()
            print ("{},{:3d}\t{},{}".format(county,delta, cases, deaths))
