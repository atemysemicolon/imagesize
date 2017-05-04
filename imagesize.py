#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May  4 14:53:50 2017

@author: valhalla
"""
from __future__ import print_function
from skimage import io
import sys

if(len(sys.argv)<=1):
    print("Supply a parameter please! -> Image location")
else:
    [filename] = sys.argv[1:]
    shp = io.imread(filename).shape
    print ("Shape (HxW)= ",shp[0:2])
    if len(shp)>2:
    	print ("Channels = ",shp[2])

