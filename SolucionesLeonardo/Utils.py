# -*- coding: utf-8 -*-
"""
Utils
Created on Wed May  6 12:12:01 2015
Common use functions
@author: lemoga
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
    
    
def ReadFasta(aPath):    
    """
    Transforms a fasta file into a dictionary of Ids -> sequences.
    
    Parameters:
    -----------
    aPath : string
        path (or name) of the FASTA file.
    
    Returns:
    -----------
    fastaDict : list
        Dictionary with the sequences
    """
    fr = open(aPath)
    dictOfsequences = {}
    seqID = ''
    seq = ''
    flag = 0
    for line in fr:
        if '>' in line:
            if flag != 0:
                dictOfsequences[seqID] = seq
                seq = ''
            seqID=line.replace('\n','')
            flag += 1
        else:
            seq += line.replace('\n','')
    dictOfsequences[seqID] = seq
    fr.close()
    return dictOfsequences

def splitBy(aString, windowSize):
    """
    Splits a sequence in pieces of windowSize.
    
    Parameters:
    -----------
    aString : string
        a string.

    windowSize : int
        word size of each piece of the string
    
    Returns:
    -----------
    stringSplit : list
        List with the pieces of windowSize of the string.
    """
    count = 0
    pos = 0
    stringSplit = []
    aPiece = ""
    while pos < len(aString):
        aPiece += aString[pos]
        count += 1
        pos += 1
        if count == windowSize:
            stringSplit.append(aPiece)
            aPiece = ""
            count = 0
    return stringSplit
