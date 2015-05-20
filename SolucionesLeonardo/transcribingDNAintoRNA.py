"""
Transcribing DNA into RNA
@author: lemoga
Let s a cDNA string and t the transcription of s
Given: s
Return: t
"""
import sys

def dna2rna(s):
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
    #Get the sequence
    fr =  open(sys.argv[1],"r")
    sequence = fr.readline()
    fr.close()
    
    #Write the answer
    fw = open(sys.argv[2],"w")
    fw.write(dna2rna(sequence))
    fw.close()
