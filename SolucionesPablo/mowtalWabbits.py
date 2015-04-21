#INPUT
I=input("Input n, m:");

n = I[0];
m = I[1];

#Aqui empieza el codigo
b=0;							# Numero de nacimientos (parejas)
W =[1];							# Lista que guarda el numero de conejos (parejas) en la posicion correspondiente a su edad en dias
for i in range(1,m+1):			# Crea la lista del tamanyo de dias correspondientes a "m", la longevidad de los conejos
	W.append(0);

for x in range(1, n):			# Loop una vez por secuencia
	b=0;						# Reinicia nacimientos
	for i in range(1,m+1):		# Calcula el numero de nacimientos (parejas) con base en los conejos adultos (parejas)
		b+=W[i];				
	for i in range(m-1,0,-1):	# Envejece los conejos un dia
		W[i]=W[i-1];			
	W[0]=b;						# Hace nacer a los conejos nuevos (parejas)

#Retornar resultado:
r=0;
for i in W:						# Sumar todos los conejos (parejas)
	r+=i;
print "wabbits: %i" %r;