#from itertools import product,chain
#from operator import itemgetter

###############################With wrong results
def EnumeratingKmersLexicographically(alphabet,n):
	myorder=dict((i,alphabet.index(i)) for i in alphabet)

	results=alphabet
	for a in range(1,n):
		resultsN=[]
		for j in (alphabet):
			resultsN.extend([i+j for i in results])
		results=resultsN+results
	
	print('\n'.join(sorted(results,key=lambda x:(myorder[x[0]],len(x)))))
	return

#################################
def extendSeq(last,alphabet,m,n):
	results=[]
	m=m+1
	for x in alphabet:
		lastTmp = last+x
		results.append(lastTmp)
		if m < n-1:
			results.extend(extendSeq(lastTmp,alphabet,m,n))
	return(results)

def EnumeratingKmersLexicographically2(alphabet,n):
	results=[]

	for x in alphabet:
		results.append(x)
		last=x
		results.extend(extendSeq(last,alphabet,0,n))
	print ('\n'.join(results))

if __name__=='__main__':
	alphabet='N I F Y G A Q T D J H'
	alphabets=alphabet.split()
	n=3
	EnumeratingKmersLexicographically2(alphabets,n)
