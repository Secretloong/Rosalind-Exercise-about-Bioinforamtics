
def MendelFirstLaw(k,m,n):
	popSize=k+m+n
	alleSize=2*(k+m+n)
	pDom=((2*k)+m)/alleSize
	pRec=((2*n)+m)/alleSize
	print(k/popSize+(m/popSize)*(k/(popSize-1))+0.75*(m/popSize)*((m-1)/(popSize-1))+0.5*(m/popSize)*(n/(popSize-1))+(n/popSize)*(k/(popSize-1))+0.5*(n/popSize)*(m/(popSize-1)))
	print (1 - ( m*n + .25*m*(m-1) + n*(n-1) ) / ( popSize*(popSize-1) )) #by sharno in Rosalind

if __name__=='__main__':
	MendelFirstLaw(2,2,2)