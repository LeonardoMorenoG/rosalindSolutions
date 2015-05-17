# Libraries
from __future__ import division; # Needed in order to avoid weird rounding practices in Python 2
from sys import argv; # Needed for receiving user input
from rosalindUtils import loadFastas; # Imports utils

# Methods
"""
Takes dictionary of sequences
Returns list with max GC content, name of sequence with max GC content
"""
def gcContent(pData):
    max = [0, 0]; # stores maximum GC
    for seq in pData.keys(): # for every sequence
        GC = 0; # Counts number of occurrences of G or C
        for j in pData[seq]: # for every letter in sequence
            if j == "G" or j == "C": # if letter is G or C
                GC += 1; # add one to GC counter
                
            if GC > max[0]: # if GC content of this sequence is greater than the previous maximum,
                max = [GC, seq]; # store this content and the sequence name as maximum
                
    max[0] = 100*max[0]/len(pData[max[1]]); # Stores GC content for this sequence as percentage
    return max;

# Run program
script, filename = argv; # From console, argv returns script name, arguments
data = loadFastas(filename); # load data

maxGC = gcContent(data);
print(maxGC[1]); # prints max GC content sequence's name
print(maxGC[0]); # prints max GC content