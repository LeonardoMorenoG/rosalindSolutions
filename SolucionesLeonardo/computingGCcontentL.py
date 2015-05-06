# -*- coding: utf-8 -*-
"""
Computing GC content
Created on Wed May  6 12:16:18 2015
Given a FASTA file returns the The ID of the string having the highest GC-content,
followed by the GC-content of that string. 
@author: lemoga
"""
import sys 
import Utils

sequences = Utils.ReadFasta(sys.argv[1])
maxPer = 0
maxId = ""

for Id in sequences:
    aSequence = sequences[Id]
    counts = Utils.countNucleotides(aSequence)
    percentage = (counts[2] + counts[3])/float(len(aSequence))*100
    if percentage > maxPer:
        maxPer = percentage
        maxId = Id

print maxId
print maxPer


