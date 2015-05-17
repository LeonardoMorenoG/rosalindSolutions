# -*- coding: utf-8 -*-
"""
Created on Sun May 17 17:55:17 2015
Methods useful in rosalind bioinformatic algorithms
@author: Palo
"""

# Libraries
from itertools import izip; # Needed to create dictionaries from lists more efficiently than zip

# Methods
"""
Takes file with multiple sequences in Fasta format, 
Returns a dictionary of keys=sequence Fasta names, values=sequences
"""
def loadFastas(pFile):
    txt = open(pFile); # Access given file
    d = txt.read(); # Read file
    
    d = d.lstrip(">"); #Remve initial >
    d = d.split(">"); #Split into separate sequences
    
    d[:] = [i.split("\n", 1) for i in d]; # Split each sequence (only first occurrence of \n) into lines: first line contains sequence name. Returns d as a list of lists (sequences) containing strings (seq name, seq).
    strNames = [i[0] for i in d]; # Stores sequence names in separate list.
    
    d[:] = [i[1].split("\n") for i in d]; # Split each sequence into its lines. Keeps only sequences. D is now a list of lists (sequences) containing strings (lines of sequence).
    d[:] = ["".join(i) for i in d]; # Join each sequence into one string (per sequence).
    
    seqDic = dict(izip(strNames, d)); # Creates dictionary with seq names as keys and seq strings as values.
    return seqDic; # returns dictionary

"""
Takes file with multiple DNA sequences separated by a newline \n escape sequence, 
Returns a list of strings (sequences)
"""
def loadSeqs(pFile):
    txt = open(pFile); # Access given file
    d = txt.read(); # Read file
    
    d = d.split("\n"); # Split each sequence into its lines. Keeps only sequences. D is now a list containing strings (sequences).    
    return d; # returns dictionary


"""
Takes two strings, 
returns list with indexes of occurrences of second string inside first
"""
def findMotif(pSeq, pMotif):
    indexes = []; # Stores indexes of all occurences of the given string
    start = 0; # Starting index for the search
    notDone = True;
    while notDone: # As long as end not reached
        index = pSeq.find(pMotif, start); # find index of motif occurrence
        if index == -1: # if not found
            notDone = False; # search done
        else: # else (if found)
            start = index+1; # Move index start number
            indexes.append(index); # store index
    
    if len(indexes) == 0: # If motif has not been found,
        indexes = "Motif not found."; # say so.
        
    return indexes;