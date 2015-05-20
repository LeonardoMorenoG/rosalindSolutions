#!/usr/bin/python
"""
Translating RNA into Protein
@author: lemoga
Created on Tue Apr  7 10:18:51 2015
Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).
       A codon Table
Return: The protein string encoded by s.
"""
import sys 

def translate_mRNA(aRNAcodonDictionary, mRNA):
    """
    Translate a mRNA into protein
    
    Parameters:
    -----------
    aRNAcodonDictionary : dictionary
        Codon Table.
    mRNA : string
        mRNA sequence
    
    Returns:
    -----------
    protein: string
        protein string encoded by mRNA
    """
    protein = ''
    x = 0
    y = 3
    while y < len(mRNA):
        actualCodon = mRNA[x:y]
        protein += rnaCondonTable[actualCodon]
        x += 3
        y += 3

    return protein
    
if __name__ == "__main__":
    #Make a dictionary with the RNA codon table
    fr = open(sys.argv[1])
    rnaCondonTable = {}
    for line in fr:
        line = line.split('\t')
        codon = line[0]
        aa = line[1].replace('\n','')
        rnaCondonTable[codon]=aa
    fr.close()
    
    
    #Get the Sequence of interest
    fr = open(sys.argv[2])
    mRNA = fr.readline()
    fr.close()
    
    #Walk through the mRNA in slides of 3
    #Save the translation in protein 
    protein = translate_mRNA(rnaCondonTable, mRNA)
    print protein 