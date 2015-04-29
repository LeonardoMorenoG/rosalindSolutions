#!/usr/bin/python
"""
Finding Motif in sequence
@author: Alejandro Reyes
v0.0 28/04/2015
Given: A file with two lines, first with ref sequence (s) and second with motif (t)
Return: A line with all locations of t as a substring of s
Usage: FindingMotif_AReyes.py file1 
"""

import sys


def countMotif(sequence): 
    """
    Counts the number of occurrences of s in t.
    Receives dictionary with t and s
    Return a list with the position (starting at 1) of each occurance of s in t
    """
    countList=[]
    found = 0
    i=0
    #print sequence['t']
    #print sequence['s']
    while i < (len(sequence['t'])-len(sequence['s'])):
        found = sequence['t'].find(sequence['s'], i)
        found=found+1
        if found == 0:
            return countList
        else:
            countList.append(found)
            i=found
    return countList


def parseFile(archivo):
    """
    Reads a two line file storing the reads in a dictionary
    Receives a filehandler of a file
    Returns a dictionary where two keys are t and s.
    """
    sequences={}
    sequences['t']=archivo.readline().strip('\n')
    sequences['s']=archivo.readline().strip('\n')
    return sequences


if __name__ == "__main__":
    #Instantiating Variables
    reads={}
    count=[]
    
    #Get the sequences
    fr =  open(sys.argv[1],"r")
    reads=parseFile(fr)
    fr.close()
    
    #Get the counts
    count=countMotif(reads)
    print ' '.join(str(x) for x in count)