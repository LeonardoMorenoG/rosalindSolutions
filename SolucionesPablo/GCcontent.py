# -*- coding: utf-8 -*-
"""
Created on ??? 2015
GC CONTENT
@author: Pablo the awesome molecular jedi
"""
# Libraries
from sys import argv; # Needed for receiving user input
from rosalindUtils import loadFastas, gcContent; # Imports utils

# Run program
script, filename = argv; # From console, argv returns script name, arguments
data = loadFastas(filename); # load data

maxGC = gcContent(data);
print(maxGC[1]); # prints max GC content sequence's name
print(maxGC[0]); # prints max GC content