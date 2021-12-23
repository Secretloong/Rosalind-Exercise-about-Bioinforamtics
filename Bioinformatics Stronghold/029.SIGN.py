from itertools import permutations

def EnumeratingOrientedGeneOrderings(n): 
	numList = []
	for i in range(1,n+1):
		numList.extend((i,-i))
	results=list(permutations(numList,n))
	res=[]
	for i in results:
		if len(set(abs(j) for j in i)) == len(i):
			res.append([str(x) for x in i])
	print(len(res))
	print('\n'.join(list(' '.join(i) for i in res)))
	return

def EnumeratingOrientedGeneOrderings2(n): #by propheta13 in Rosalind
	lst = [x for x in permutations([i for i in range(-n,n+1) if (i != 0)], n) if set(range(1, n+1)) == set(map(abs,x))]
	print (len(lst))
	for i in lst:
		print (" ".join(map(str,i)))

if __name__=='__main__':
	EnumeratingOrientedGeneOrderings(6)