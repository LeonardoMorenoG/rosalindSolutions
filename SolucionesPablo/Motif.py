# -*- coding: utf-8 -*-
"""
Created on Sun May 17 13:18:43 2015
FINDING A MOTIF
@author: Palo
"""
# Libraries
from sys import argv; # Needed for receiving user input
from rosalindUtils import loadSeqs, findMotif; # Imports utils

# Run program
script, filename = argv; #From console, argv returns script name, arguments
data = loadSeqs(filename); # Loads list of sequences. Sequence in position 0, motif in key 1.

motifs = findMotif(data[0],data[1]); # finds indexes of motif in seq.
m = [str(i+1) for i in motifs]; # converts indexes to strings. Increases index number by one due to solution constraints

print(" ".join(m)); # Prints indexes as string separated by a space character