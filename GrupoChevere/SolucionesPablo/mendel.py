k = float(18);
m = float(20);
n = float(17);
t = float(k+m+n);

p = k/t + (k*(m+n)+0.75*m*(m-1)+m*n)/(t*(t-1));
q = 1 - (n*(n-1) + n*m + 0.25*m*(m-1))/(t*(t-1));

print p;
print q;