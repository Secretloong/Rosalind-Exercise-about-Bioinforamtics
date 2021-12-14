from itertools import product

def permutedCycle(a,alphabet):
	cycle=[]
	for i in range(len(alphabet)):
		cycle.append(a+alphabet[i])
	return (cycle)

def EnumeratingKmersLexicographically(alphabet,n):
	results=alphabet
	for a in range(1,n):
		resultsN=[]
		for j in (alphabet):
			resultsN.extend([i+j for i in results])
		results=resultsN[:]
	
	## sort() modifies the list in-place (and returns None to avoid confusion)
	#results.sort()
	#print('\n'.join(results))
	
	print('\n'.join(sorted(results)))
	return

if __name__=='__main__':
	alphabet='A B C D E F G H'.split()
	EnumeratingKmersLexicographically(alphabet,3)

	#by Richard Smith in Rosalind, cartesian product, equivalent to a nested for-loop
	print ('\n'.join([''.join(x) for x in product(alphabet,repeat=3)]))