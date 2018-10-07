#!/usr/bin/python2
# -*- coding: utf-8 -*-
def subsets(n):
    subset = [[]]
    for i in n:
        subset.extend([x + [i] for x in subset])
    return subset
    
a=subsets(['Human','Tree','Wolf','Pig'])
print a
