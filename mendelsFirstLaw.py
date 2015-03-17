#Primera ley de mendel 

import sys

def mendel (m,k,n):

	total= k+m+n

	apareamientos= total* (total-1)/2

	m_m= m*(m-1)/2
	m_k= m*k
	m_n= m*n
	k_k= (k*(k-1)/2)*0.75
	k_n= 0.5*(k*n)

	posibles= m_m+m_k+m_n+k_k+k_n

	return posibles/apareamientos

print mendel (int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]))