# -*- coding: utf-8 -*-
"""
Created on Mon Feb 05 22:25:48 2018

@author: Wu Jingwei
"""

# Read from the file file.txt and output the tenth line to stdout.
awk 'NR==10{print}' file.txt
sed -n '10p' file.txt