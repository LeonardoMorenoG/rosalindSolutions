#!/usr/bin/python
"""
Computing GC content
@author: laurag
v1.0 06/05/2015
Let s DNA strings
Given: A set of DNA strings s[]
Return: The DNA with highest GC content
Usage python program file1 file2
"""

import sys

def gccontent(s):
    """
    Compute DNA GC content
    
    Parameters:
    -----------
    s : string
        cDNA sequence.
    
    Returns:
    -----------
	GC : float
	    GC content
	"""

    count=0.0
    perc=0.0
    size=len(s)
    for i in s:
        if i == 'C' or  i == 'G':
            count += 1
    gc= (count / size)* 100
    return(gc)
  	
if __name__ == "__main__":
   
    #Instantiating Variables
	IDs=[]
	DNA=[]
	CONT=[]
	DIC= dict()
	
    #Get the sequences and ids
   
	fr =  open(sys.argv[1],"r")
	for line in fr:
		if line.startswith('>'):
			IDs.append(line.strip('>\n'))
		else:
			DNA.append(line.strip('>\n'))
	fr.close()

    
    #Compute GC content
	for j in DNA:
		CONT.append(gccontent(j))

	for k in range(0,len(IDs)):
		DIC[CONT[k]]=IDs[k]

	#Compute GC content
	fw = open(sys.argv[2],"w")
	fw.write(DIC[max(CONT)]+' '+format(round(max(CONT),6)))
	fw.close()