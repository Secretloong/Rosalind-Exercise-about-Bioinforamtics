from itertools import permutations
import math

def PartialPermutations(n,k): #with exit code -9
	results=list(permutations([i for i in range(1,n+1)],k))
	print(len(results)%1000000)
	return

def PartialPermutations2(n,k):
	#𝑛!/(𝑛−𝑚)!
	results=math.factorial(n)/math.factorial(n-k)
	print(int(results%1000000))

def PartialPermutations3(n,k):
	#𝑛(𝑛−1)(𝑛−2)...(𝑛−𝑚+1)
	results=1
	for i in range(k):
		results *= n - i
		results %= 10**6
	print (results)

if __name__=='__main__':
	PartialPermutations2(97,9)