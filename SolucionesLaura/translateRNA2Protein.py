#!/usr/bin/python
"""
Translating mRNA into Protein
@author: laurag
v1.0 06/05/2015
Let s a mRNA string
Given: A mRNA string s 
Return: A Protein String p using a dictionary of codons
Usage python program file1 file2
"""

import sys

def translate(s): 
	"""
    Transcribe cDNA into RNA
    
    Parameters:
    -----------
    s : string
        cDNA sequence.
    
    Returns:
    -----------
	t : string
	    RNA sequence
	"""
	dict = {'CGA':'R','UUU':'F','UUC':'F','UUA':'L','UUG':'L','UCU':'S','UCC':'S','UCA':'S','UCG':'S','UAU':'Y','UAC':'Y','UAA':'Stop','UAG':'Stop','UGU':'C','UGC':'C','UGA':'Stop','UGG':'W','CUU':'L','CUC':'L','CUA':'L','CUG':'L','CCU':'P','CCC':'P','CCA':'P','CCG':'P','CAU':'H','CAC':'H','CAA':'Q','CAG':'Q','CGU':'R','CGC':'R','AGA':'R','CGG':'R','AUU':'I','AUC':'I','AUA':'I','AUG':'M','ACU':'T','ACC':'T','ACA':'T','ACG':'T','AAU':'N','AAC':'N','AAA':'K','AAG':'K','AGU':'S','AGC':'S','GGA':'G','AGG':'R','GUU':'V','GUC':'V','GUA':'V','GUG':'V','GCU':'A','GCC':'A','GCA':'A','GCG':'A','GAU':'D','GAC':'D','GAA':'E','GAG':'E','GGU':'G','GGC':'G','GGG':'G'}
	
	p = ""
	l = len(s)/3
	for i in range(1,l):
  		codon = s[i*3-3:i*3]
  		amino = dict[codon]
  		p = p + amino
	return p
  	
if __name__ == "__main__":
   
    #Instantiating Variables
    sequence = ""
    
    #Get the sequence
    fr =  open(sys.argv[1],"r")
    sequence = fr.readline()
    fr.close()
    
    #Transcribe and Write the file
    fw = open(sys.argv[2],"w")
    fw.write(translate(sequence))
    fw.close()
