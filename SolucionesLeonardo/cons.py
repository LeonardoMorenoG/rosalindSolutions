#!/usr/bin/python
"""
Consensus and Profile
Created on Tue Apr  7 11:36:27 2015
@author: lemoga
Let m a matrix of sequences; p(m) a profile matrix of m  & cs(m) a consensus 
string of m. 
Given: m
Reuturn: p(m) & one cs(m)
Usage: python cons.py inFile.fasta outfile.txt
"""

import sys
import Utils


def Consensus(m):
    """
    Counts the number of each nucleotide in a sequence.
    
    Parameters:
    -----------
    m : stringMatrix
        Matrix of sequences
    
    Returns:
    -----------
    Obj : [Matrix, string]
        [ProfileTransposed, oneConsensus]
    """
    allColumns = []
    for i in range(0,len(sequencesMatrix[0])):
        column = []    
        for sequence in sequencesMatrix:
            column.append(sequence[i])
        allColumns.append(column)
        
    transposedProfile = []
    consensus = []
    for column in allColumns:
        aColumn = ''    
        for element in column:
            aColumn += element
        dictProfileC = Utils.countNucleotides(aColumn)
        profileC = [dictProfileC["A"],dictProfileC["C"],dictProfileC["G"],dictProfileC["T"]]
        transposedProfile.append(profileC)
        indexHF = profileC.index(max(profileC))
        print profileC
        if indexHF == 0:
            consensus.append('A')
        elif indexHF == 1:
            consensus.append('C')
        elif indexHF == 2:
            consensus.append('G')
        else:
            consensus.append('T')
    return [transposedProfile, consensus]
    
if __name__ == "__main__":
    #Read Fasta File
    sequences = Utils.ReadFasta(sys.argv[1])
    
    #Create Matrix of Sequences
    sequencesMatrix = []
    for key in sequences:
        sequencesMatrix.append(sequences[key])
    
    #Obtein a Profile and one consensus sequence
    answer = Consensus(sequencesMatrix)
    transposedProfile = answer[0]
    consensus = answer[1]
    
    #Write a file with the answer
        #Write the consensus
    fw = open(sys.argv[2],"w")
    for nt in consensus:
        fw.write(nt)
    fw.write('\n')
        #Write the profile
    for i in range(0,len(transposedProfile[0])):
        #if i%2 == 0:
        for row in transposedProfile:
            fw.write(str(row[i]) + " ")
        fw.write('\n')
    fw.close()