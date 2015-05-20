#!/usr/bin/python
"""
Finding a Motif in DNA
@author: lemoga
Created on Tue Apr  7 11:09:50 2015
Let s a sequence of DNA & m a motif or pattern. Find if p is in s
Given: s & p
Return: all locations of p in s
"""
import sys 

def findMotif(aSequence, aMotif):
    """
    Counts the number of each nucleotide in a sequence.
    
    Parameters:
    -----------
    aSequence : string
        DNA sequence.
    aMotif : string
        DNA sequence < aSequence        
    
    Returns:
    -----------
    locations : string
        All locations of aMotif as a substring of aSequence
    """
    #Identify the window size
    lm = len(aMotif)
    x = 0
    y = lm
    #walk the sequence through a windows and identify the locations
    locations = ''
    while y < len(aSequence):
        lm_mer = aSequence[x:y]
        if lm_mer == aMotif:
            l = x+1
            locations += (str(l) + ' ')
        x += 1
        y += 1
    return locations

if __name__ == "__main__":
    
    fr = open(sys.argv[1])
    sequence = fr.readline().replace('\n','')
    motif = fr.readline().replace('\n','')
    
    print findMotif(sequence, motif)
    