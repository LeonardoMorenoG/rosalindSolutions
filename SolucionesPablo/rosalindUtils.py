# -*- coding: utf-8 -*-
"""
Created on Sun May 17 17:55:17 2015
Methods useful in rosalind bioinformatic algorithms
@author: Pablo the awesome molecular jedi
"""

# Libraries
from __future__ import division; # Needed in order to avoid weird rounding practices in Python 2
from itertools import izip; # Needed to create dictionaries from lists more efficiently than zip

# Methods
"""
Takes file with multiple sequences in Fasta format, 
Returns a dictionary of keys=sequence Fasta names, values=sequences
"""
def loadFastas(pFile):
    txt = open(pFile); # Access given file
    d = txt.read(); # Read file
    
    d = d.lstrip(">"); #Remve initial >
    d = d.split(">"); #Split into separate sequences
    
    d[:] = [i.split("\n", 1) for i in d]; # Split each sequence (only first occurrence of \n) into lines: first line contains sequence name. Returns d as a list of lists (sequences) containing strings (seq name, seq).
    strNames = [i[0] for i in d]; # Stores sequence names in separate list.
    
    d[:] = [i[1].split("\n") for i in d]; # Split each sequence into its lines. Keeps only sequences. D is now a list of lists (sequences) containing strings (lines of sequence).
    d[:] = ["".join(i) for i in d]; # Join each sequence into one string (per sequence).
    
    seqDic = dict(izip(strNames, d)); # Creates dictionary with seq names as keys and seq strings as values.
    return seqDic; # returns dictionary


"""
Takes file with multiple DNA sequences separated by a newline \n escape sequence, 
Returns a list of strings (sequences)
"""
def loadSeqs(pFile):
    txt = open(pFile); # Access given file
    d = txt.read(); # Read file
    
    d = d.split("\n"); # Split each sequence into its lines. Keeps only sequences. D is now a list containing strings (sequences).    
    return d; # returns dictionary


"""
Output data to output.txt in Output folder.
"""
def output(out):
    fOut = open("Output/output.txt","w+"); # create or open file in writing mode
    fOut.write(out); # write output to file
    fOut.close(); # close file


"""
Takes two strings, 
returns list with indexes of occurrences of second string inside first
"""
def findMotif(pSeq, pMotif):
    indexes = []; # Stores indexes of all occurences of the given string
    start = 0; # Starting index for the search
    notDone = True;
    while notDone: # As long as end not reached
        index = pSeq.find(pMotif, start); # find index of motif occurrence
        if index == -1: # if not found
            notDone = False; # search done
        else: # else (if found)
            start = index+1; # Move index start number
            indexes.append(index); # store index
    
    if len(indexes) == 0: # If motif has not been found,
        indexes = "Motif not found."; # say so.
        
    return indexes;


"""
Counts As, Ts, Cs, and Gs in DNA sequence. Returns dictionary with nucleotides as keys.
"""
def count(seq):
    atcg = {"A":seq.count("A"), "T":seq.count("T"), "G":seq.count("G"), "C":seq.count("C")};
    return atcg;


"""
Takes dictionary of keys=sequence Fasta names, values=sequences
Returns list with max GC content, name of sequence with max GC content
"""
def gcContent(pData):
    max = [0, 0]; # stores maximum GC
    for seq in pData.keys(): # for every sequence
        GC = 0; # Counts number of occurrences of G or C
        for j in pData[seq]: # for every letter in sequence
            if j == "G" or j == "C": # if letter is G or C
                GC += 1; # add one to GC counter
                
            if GC > max[0]: # if GC content of this sequence is greater than the previous maximum,
                max = [GC, seq]; # store this content and the sequence name as maximum
                
    max[0] = 100*max[0]/len(pData[max[1]]); # Stores GC content for this sequence as percentage
    return max;


"""
Takes dictionary of keys=sequence Fasta names, values=sequences
Return dictionary with { consensus: consensus sequence (string), nucleotide: profile (list of nucleotide frequency in each position)
"""
def consensus(data):
    l = len(data.values()[0]); # Stores length of DNA sequences analyzed
    C = { "consensus":"", "A":[0]*l, "T":[0]*l, "C":[0]*l, "G":[0]*l } # Dictionary with consensus sequence and lists of size l, stores consensus sequence and occurrences of nucleotide in all sequences for each position
    
    # Build profile matrix:
    for seq in data.values(): # For every sequence
        for b in range(0,l): # For every base in sequence
            C[seq[b]][b] = C[seq[b]][b] + 1; # Add one to count of corresponding nucleotide at corresponding position
    
    # Build consensus sequence:
    for p in range(0,l): # For every position in sequence
        S = { C["A"][p]:"A", C["T"][p]:"T", C["C"][p]:"C", C["G"][p]:"G" } # Define a dictionary that relates the number of occurrences in all sequences of each nucleotide at the current position to the nucleotide's letter
        C["consensus"] = C["consensus"] + S[max(S.keys())]; # Adds nucleotide letter with most occurrences at this position to the consensus sequence
    
    return C;


"""
Transcribes DNA to RNA
"""
def transcribe(dna):
    rna = dna.replace("T", "U");
    return rna;


"""
Returns genetic code dictionary. Stop codons are "*"
"""
def geneticCode():
    code = {'CGA':'R','UUU':'F','UUC':'F',
      'UUA':'L','UUG':'L','UCU':'S',
      'UCC':'S','UCA':'S','UCG':'S',
      'UAU':'Y','UAC':'Y','UAA':'*',
      'UAG':'*','UGU':'C','UGC':'C',
      'UGA':'*','UGG':'W','CUU':'L',
      'CUC':'L','CUA':'L','CUG':'L',
      'CCU':'P','CCC':'P','CCA':'P',
      'CCG':'P','CAU':'H','CAC':'H',
      'CAA':'Q','CAG':'Q','CGU':'R',
      'CGC':'R','AGA':'R','CGG':'R',
      'AUU':'I','AUC':'I','AUA':'I',
      'AUG':'M','ACU':'T','ACC':'T',
      'ACA':'T','ACG':'T','AAU':'N',
      'AAC':'N','AAA':'K','AAG':'K',
      'AGU':'S','AGC':'S','GGA':'G',
      'AGG':'R','GUU':'V','GUC':'V',
      'GUA':'V','GUG':'V','GCU':'A',
      'GCC':'A','GCA':'A','GCG':'A',
      'GAU':'D','GAC':'D','GAA':'E',
      'GAG':'E','GGU':'G','GGC':'G',
      'GGG':'G' 
      };
    return code;


"""
Translates RNA to protein (takes rna string, returns peptide string).
"""
def translate(seq):
    code = geneticCode(); # Stores genetic code
    pep = ""; # stores peptide sequence
    i = 0; # position on RNA sequence
    while i < len(seq): # for every codon
        codon = seq[i:(i+3)]; # get current codon
        aa = code[codon]; # get aminoacid
        if (aa != "*"): # if not a stop codon
            pep = pep + aa; # add residue to peptide
            i = i+3; # next codon
        else: # if codon is stop
            i = len(seq); # stop loop
    return pep;