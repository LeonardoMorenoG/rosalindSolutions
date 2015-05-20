#!/usr/bin/python
"""
Counting point mutations
Created on Tue Apr  7 09:21:05 2015
@author: lemoga

Determine the number of mutations as the Hamming Distance of two sequences
Input: A file with two nucleotide sequences s and t : strings
Output: Hamming distance between s and t : int
"""

import sys 
import itertools
"""
+Avoids the use of index i
+Creates an iterator, not the list of tuples in memory
"""
def hammingDistance(s, t):
    value = 0
    for a, b in itertools.izip(s, t):
        if a != b: value += 1
    return value  

if __name__ == "__main__":
    fr = open(sys.argv[1], "r")
    seqA = fr.readline()
    seqB = fr.readline()
    fr.close()
    
    countMutations =  hammingDistance(seqA, seqB)
    
    print countMutations