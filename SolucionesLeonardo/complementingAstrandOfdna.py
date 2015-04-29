"""
Let s a DNA string and sc The reverse complement of s
Given:  s of length at most 1000 bp.
Return: sc.
"""
import sys 

def complementStrand(aStrand):
    """
    Make the reverse complement of a DNA sequence
    
    Parameters:
    ----------
    aStrand : string
        a strand of DNA
    
    Returns:
    --------
    sc : string
        reverse complement of aStrand
    """
    cdna = ""
    for nucleotide in aStrand:
        if nucleotide == "A":
            cdna += "T"
        elif nucleotide == "T":
            cdna += "A"
        elif nucleotide == "C":
            cdna += "G"
        elif nucleotide == "G":
            cdna += "C"
    cdna = cdna[::-1]
    return cdna

#Get the sequence
fr = open(sys.argv[1],"r")
dna = fr.readline()
fr.close()

#Write the answer
fw = open(sys.argv[2],"w")
fw.write(complementStrand(dna))
fw.close()

"""
I could do this
dna.replacce("A","a").replace("T","a").replace("G","c").replace("C","g").upper()
and then print dna[::-1]
"""
