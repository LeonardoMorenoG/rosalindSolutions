#!/usr/bin/python
"""
Computing GC content
@author: lemoga
Created on Wed May  6 12:16:18 2015
Given a FASTA file returns the The ID of the string having the highest GC-content,
followed by the GC-content of that string. 
"""
import sys 
import Utils

sequences = Utils.ReadFasta(sys.argv[1])
maxPer = 0
maxId = ""

if __name__ == "__main__":
    for Id in sequences:
        aSequence = sequences[Id]
        counts = Utils.countNucleotides(aSequence)
        percentage = (counts["G"] + counts["C"])/float(len(aSequence))*100
        if percentage > maxPer:
            maxPer = percentage
            maxId = Id
    
    print maxId
    print maxPer