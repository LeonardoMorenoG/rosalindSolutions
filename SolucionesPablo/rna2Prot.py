# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 13:36:16 2015
TRANSLATING RNA TO PROTEIN
@author: Pablo the awesome molecular jedi
"""

# Libraries
from sys import argv; # Needed for receiving user input
from rosalindUtils import loadSeqs, translate; # Imports utils

# Run program
script, filename = argv; #From console, argv returns script name, arguments
data = loadSeqs(filename); # Loads list of sequences. Sequence in position 0.
seq = data[0]; # gets sequence string

pep = translate(seq); # translate sequence to peptide
print(pep);