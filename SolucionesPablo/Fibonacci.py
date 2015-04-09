n = input("Encontrar el n-esimo termino de la sucesion Fibonacci para n igual a: ");

s=0;
d=0;
f=1;

for i in range(0,n-1):
	s=f;
	f=f+d;
	d=s;

print "El termino %i de la sucesion Fibonacci es: %i." % (n, f);