# -*- coding: utf-8 -*-
"""
Utils
Created on Thu Apr  9 07:51:29 2015
@author: lemoga
Contains frequently used functions 
"""

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

