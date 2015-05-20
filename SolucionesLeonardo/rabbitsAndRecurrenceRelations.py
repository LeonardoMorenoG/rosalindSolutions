#!/usr/bin/python
"""
rabbitsAndRecurrenceRelations
@author: lemoga
v1.0 07/04/2015
Given: Positive integers n<=40 and k<=5
Return: The total number of rabbit pairs that will be present after n months if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).
Use: python rabbitsAndRecurrenceRelations.py months litter outFile"""

import sys

def rabbits(n,k):
    """
    Computes the total number of rabbit pairs that will be present after n months if we begin with 1 pair and in each generation.
    Every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).
    
    Parameters:
    -----------
    n : int
        months.
    k : int
        litter
    
    Returns:
    -----------
    rabbits : int
        Total number of rabbits
    """
    if n == 1 or n == 2:
        return 1
    else:
        return rabbits(n-1,k) + rabbits(n-2,k)*k

if __name__ == "__main__":
    months = int(sys.argv[1])
    litter = int(sys.argv[2])
    fw = open(sys.argv[3],"w")
    fw.write(str(rabbits(months, litter)))
    fw.close()
