from itertools import permutations

def EnumeratingGeneOrders(n):
	results=list(permutations([i for i in range(1,n+1)],n))
	print(len(results))
	for i in results:
		i = [str(j) for j in i]
		print (' '.join(i))
	return

if __name__=='__main__':
	EnumeratingGeneOrders(6)