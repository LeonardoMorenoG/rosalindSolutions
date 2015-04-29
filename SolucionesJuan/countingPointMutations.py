'''
1.0 Importando modulos
'''

from itertools import islice

'''
2.0 Prealocando las variables
'''

seqs=[]
count=0

'''
3.0 Leer el archivo y extraer las secuencias
'''

with open('/home/juancastro/Downloads/testPM.txt') as archivo:
    for i in archivo:
        seqs.append(i.strip('>\n'))

seq1=seqs[0]
seq2=seqs[1]

'''
4.0 Contar mutaciones puntuales
'''

for j in range(0,len(seq1)):
    if seq1[j] == seq2[j]:
        count = count
    else :
        count = count + 1

print(count)
    

