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

    count = [0,0,0,0]
    for nucleotide in aSequence:
        if nucleotide == "A":
            count[0] += 1
        elif nucleotide == "C":
            count[1] += 1            
        elif nucleotide == "G":
            count[2] += 1            
        elif nucleotide == "T":
            count[3] += 1
    finalCount = {"A":count[0],"C":count[1],"G":count[2],"T":count[3]}
    return finalCount


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
