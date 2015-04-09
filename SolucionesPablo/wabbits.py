n = 28;
k = 5;

q = 1;
w = 1;
e = 0;

for x in range(0, n-2):
	e = w + q*k;
	q = w;
	w = e;

print "wabbits:";
print w;