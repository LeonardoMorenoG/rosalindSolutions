#!/usr/bin/python
"""
Counting Nucleotides
@author: lemoga
v1.0 07/04/2015
Let s a DNA string
Given: A DNA string s 
Return: A file with four integers (separated by spaces) counting the respective
        number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.
Usage python name file1 file2
"""

import sys


def countNucleotides(aSequence): 
    """
    Counts the number of each nucleotide in a sequence.
    
    Parameters:
    -----------
    aSequence : string
        DNA sequence.
    
    Returns:
    -----------
    count : list
        List with the number of each nucleotide in a sequence. The order is A T G C
    """
    count = []
    count.append(aSequence.count("A"))
    count.append(aSequence.count("T"))
    count.append(aSequence.count("G"))
    count.append(aSequence.count("C"))
    return count

if __name__ == "__main__":
    #Instantiating Variables
    sequence = ""
    count = []
    
    #Get the sequence
    fr =  open(sys.argv[1],"r")
    sequence = fr.readline()
    fr.close()
    
    #Get the count and Write the file
    count = countNucleotides(sequence)
    fw = open(sys.argv[2],"w")
    for nt in count:
        fw.write(str(nt) + ', ')
    fw.close()
