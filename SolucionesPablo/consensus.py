# -*- coding: utf-8 -*-
"""
Created on Sun May 17 20:40:13 2015
CONSENSUS & PROFILE
@author: Pablo the awesome molecular jedi
"""

# Libraries
from sys import argv; # Needed for receiving user input
from rosalindUtils import loadFastas, consensus, output; # Imports utils

# Run program
script, filename = argv; # From console, argv returns script name, arguments
data = loadFastas(filename); # load data

D = consensus(data); # Return dictionary with consensus: consensus sequence (string) and each nucleotide as a key to its profile (list)

T = "T: " + " ".join( [ str(i) for i in D["T"] ] );
G = "G: " + " ".join( [ str(i) for i in D["G"] ] );
A = "A: " + " ".join( [ str(i) for i in D["A"] ] ); # Required output format
C = "C: " + " ".join( [ str(i) for i in D["C"] ] );

output(D["consensus"] + "\n" + A + "\n" + C + "\n" + G + "\n" + T); # string stores output for writing to file