#!/usr/bin/python
"""
Finding Consensus and Profile in sequence
@author: Alejandro Reyes
v0.0 20/05/2015
Given: A file with n Fasta sequences, all with length m
Return: A line with the consensus and a matrix with the profile
Usage: FConsensusProfile.py file1 
"""

import sys

def countNuc(sequence): 
    """
    Generates the matrix profile given a set of sequences.
    
    Parameters:
    -----------
    sequence : dictionary of DNA sequences
    
    Returns:
    -----------
    count : two dimmensional array with the counts. 0:A, 1:C,2:G,3:T

    """
    count=dict()
    seq=0
    for names in sequence.keys():
        for i in range(len(sequence[names])):
            nuc=0
            if (seq==0):
                count[i]=[0,0,0,0]
            if (sequence[names][i]=="C"):
                nuc=1
            elif(sequence[names][i]=="G"):
                nuc=2
            elif(sequence[names][i]=="T"):
                nuc=3
            #print "i es %s nuc es %s" % (i, nuc)
            count[i][nuc]+=1
        seq=1
    return count


def GenConsensus(matrix):
    """
    Generates the consensus sequence from a stored matrix
    
    Parameters:
    ----------
    matrix: A two dimensional dictionary with the lengths and characters as keys
    
    Returns:
    --------
    consensus: A string with the consensus
    """
    consens=[]
    for l in range(len(matrix)):
        cons="A"
        max_count=0
        #print "l es %d counts son %d,%d,%d,%d" % (l, matrix[l][0],matrix[l][1],matrix[l][2],matrix[l][3])
        if(matrix[l][0] > max_count):
            cons="A"
            max_count=matrix[l][0]
        if(matrix[l][1] > max_count):
            cons="C"
            max_count=matrix[l][1]
        if(matrix[l][2] > max_count):
            cons="G"
            max_count=matrix[l][2]
        if(matrix[l][3] > max_count):
            cons="T"
            max_count=matrix[l][3]
        consens.append(cons)
    consensus="".join(consens)
    return consensus


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
    reads={}
    array_count=[]

 
    #Get the sequences
    fr =  open(sys.argv[1],"r")
    reads=parseFastaFile(fr)
    fr.close()
    
    #Get the counts
    matrix=countNuc(reads)
    consensus_main=GenConsensus(matrix)
        
    print consensus_main
    A_line=["A:"]
    C_line=["C:"]
    G_line=["G:"]
    T_line=["T:"]
    for l in range(len(matrix)):
        A_line.append(matrix[l][0])
        C_line.append(matrix[l][1])
        G_line.append(matrix[l][2])
        T_line.append(matrix[l][3])
    print " ".join([str(i) for i in A_line])
    print " ".join([str(i) for i in C_line])
    print " ".join([str(i) for i in G_line])
    print " ".join([str(i) for i in T_line])