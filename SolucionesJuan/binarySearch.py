'''
1.0 Cargando modulos
'''
from itertools import islice

'''
2.0 Prealocando variables
'''
listaIndice=[]

'''
3.0 Definiendo funcion para partir cadenas de caracteres en arreglos
'''

def split_line(text):
    # split the text
    lista=[]
    words = text.split()
    return(words)

'''
4.0 Cragando archivo linea por linea
'''

with open ('/home/juancastro/Downloads/testBIN.txt') as archivo:
    contenido=archivo.readlines()

'''
5.0 Crear 4 diferentes arreglos
'''
tamanoIndice=contenido[0].strip('\n')
tamanoArreglo=contenido[1].strip('\n')
indice=split_line(contenido[2])
indice[-1].strip('\n')
arreglo=split_line(contenido[3])
arreglo[-1].strip('\n')

'''
6.0 Determinar indices en arreglos busqueda binaria
'''
for i in arreglo:
    if i in indice:
        for j in range(0,len(indice)):
            if i == indice[j]:
                listaIndice.append(j+1)
    else:
        listaIndice.append(-1)

'''
7.0 Formatendo la salida
'''

string=""
space=" "
for i in range(0,len(listaIndice)):
    string=string +str(listaIndice[i])
    string=string+space
               
print string
