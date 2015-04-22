#!/usr/bin/python
# developed by Alejandro Reyes

from optparse import OptionParser
import sys, string, pdb, sys, os

'''
1.0 Declaracion de las variables
'''
IDs=[]
DNA=[]
CONT=[]
DIC= dict()

'''
2.0 Definicion de funciones
'''

def gccontent(str):
    count=0.0
    perc=0.0
    size=len(str)
    for i in str:
        if i == 'C':
            count += 1
        elif i == 'G':
            count = count + 1
    perc= (count / size)* 100
    return(perc)

'''
3.0 Definicion de opciones y ayuda
'''
usage = 'usage: %prog [options] arg'
parser = OptionParser(usage)
parser.add_option('-s', dest='seqs_file', help='Sequence file')
parser.add_option('-p', dest='predict_file', help='Gene predictions file')
parser.add_option('-o', dest='output_file', help='Output amino acid fasta file')
(options,args) = parser.parse_args()





'''
3.0 Leer el archivo y extraer IDs y las secuencias
'''
    
with open('/home/juancastro/Downloads/testGC.txt') as archivo:
    for linea in archivo:
        if linea.startswith('>'):
            IDs.append(linea.strip('>\n'))
        else:
            DNA.append(linea.strip('>\n'))


'''
4.0 Calcular porcentaje GC
'''
for j in DNA:
    CONT.append(gccontent(j))

for k in range(0,len(IDs)):
    DIC[CONT[k]]=IDs[k]

'''
5.0 Imprimir el nombre y el valor
'''


print DIC[max(CONT)]

print"{0:.6f}".format(round(max(CONT),6))


    

            

