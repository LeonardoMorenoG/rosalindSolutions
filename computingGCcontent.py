'''
1.0 Prealocando las variables
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


    

            

