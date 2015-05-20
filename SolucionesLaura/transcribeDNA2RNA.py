#!/usr/bin/python
"""
Transcribing cDNA into mRNA
@author: laurag
v1.0 06/05/2015
Let s a cDNA string
Given: A cDNA string s 
Return: An RNA string t, converting T into U
Usage python program file1 file2
"""

import sys

def transcribe(s): 
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
    t = s.replace("T","U")
    return t 
    
if __name__ == "__main__":
   
    #Instantiating Variables
    sequence = ""
    
    #Get the sequence
    fr =  open(sys.argv[1],"r")
    sequence = fr.readline()
    fr.close()
    
    #Transcribe and Write the file
    fw = open(sys.argv[2],"w")
    fw.write(transcribe(sequence))
    fw.close()
