
def MortalFibonacciRabbits(n,k,m):
	populations=[1,1]
	for i in range(2,n):
		if i==m:
			populations.append(populations[i-2]*k + populations[i-1] - populations[i-m]) #the first generation, effected by maturation time
		elif i>m:
			populations.append(populations[i-2]*k + populations[i-1] - populations[i-m-1]*k) #new born in (i-m)+1 generation
		else:
			populations.append(populations[i-2]*k + populations[i-1])
	print(populations)
	print(populations[-1])

def fib(n,k,m): #by abeliangrape in Rosalind: keep track of the ages of the rabbits and their populations
	ages = [1] + [0]*(m-1) # [1,0,0] the number of one month old, two and three ...
	for i in range(n-1):
		ages = [sum(ages[1:])*k] + ages[:-1] # two month could produce offspring, and three month died
	print (ages)
	print (sum(ages))

if __name__=='__main__':
	MortalFibonacciRabbits(6,1,3)
	fib(6,1,3)