#!/usr/bin/python
"""
Computing GC content
@author: Alejandro Reyes
v0.0 28/04/2015
Given: A fasta formatted file with multiple DNA sequences 
Return: A line with the ID of the string having the highest GC-content, followed by the GC-content of that string.
Usage: countigGC_AReyes.py file1 
"""

import sys


def countGC(sequence): 
    """
    Counts the number of G's or C's in a sequence.
    
    Parameters:
    -----------
    sequence : string
        DNA sequence.
    
    Returns:
    -----------
    count : string
        Frequency of G'c and C's in the sequence.
    """
    gc=0.0
    total=len(sequence)
    for i in sequence:
        if i in ("G", "C"):
            gc+=1
    return (gc/total)*100


def parseFastaFile(archivo):
    """
    Reads a fasta file storing the reads in a dictionary
    Receives a filehandler of a fasta file
    Returns a dictionary where the fasta header (without the ">") is the key and the sequence is the value.
    """
    sequences={}
    name=""
    for line in archivo:
        if line.startswith('>'):
            name=line.strip('>\n')
            sequences[name]=""
        else:
            sequences[name]=sequences[name]+line.strip('\n')
    return sequences        


if __name__ == "__main__":
    #Instantiating Variables
    per_gc = ""
    reads={}
    max_count=0
    max_name=""
    count=0
    
    #Get the sequences
    fr =  open(sys.argv[1],"r")
    reads=parseFastaFile(fr)
    fr.close()
    
    #Get the counts
    for names in reads.keys():
        count=countGC(reads[names])
        if count > max_count:
            max_count=count
            max_name=names
        
    print max_name
    print max_count