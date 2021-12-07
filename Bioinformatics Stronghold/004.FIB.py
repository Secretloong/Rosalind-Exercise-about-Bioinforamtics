
def FibonacciRabbits(n,k):
	populations=[]
	for i in range(0,n):
		if i <= 1:
			populations.append(1)
		else:
			populations.append(populations[i-1]+(populations[i-2]*k))
	print (populations[n-1])

def fib(n, k): #by Kit Burschka on Rosalind
    a, b = 1, 1
    for i in range(2, n):
        a, b = b, k*a + b
    return b

if __name__=='__main__':
	FibonacciRabbits(5,3)
	print(fib(5,3))