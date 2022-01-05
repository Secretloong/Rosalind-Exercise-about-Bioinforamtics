from Bio import SeqIO
#import math

##########My answer is wrong, there is invalid matching when any side has no equal AU or CG##########
def RNASecondaryStructures(s):
	print(CatalanNumbers(s.count('A'),{})*CatalanNumbers(s.count('G'),{})%1000000)
	return

def CatalanNumbers(n,dp): #nodes: 2n; memorizer (dp) cound speed up building
	if n==0 or n==1:
		res=1
	elif n in dp.keys():
		return (dp[n])
	else:
		res=0
		for k in range(1,n+1):
			res=res+(CatalanNumbers(k-1,dp)*CatalanNumbers(n-k,dp))
		dp[n]=res%1000000
	return (res%1000000)

##########https://gist.github.com/adijo/59f3c814cbc17db2506d##########
def RNASecondaryStructures2(rna, lo, hi, dp):
	mapping = {
	"A" : "U",
	"U" : "A",
	"G" : "C",
	"C" : "G"
	}
	characters = hi - lo + 1
    
	# if there are an odd number of nucleotides, 
	# this is an invalid matching.
	if characters % 2 == 1:
		return 0

	# handles tricky edge cases.
	if lo >= hi or lo >= len(rna) or hi < 0:
		return 1

	# return answer if it is memoized.    
	if (lo, hi) in dp:
		return dp[(lo, hi)]
	else:
		curr = rna[lo]
		target = mapping[curr]
		acc = 0
		#we must match all the edges on one side of {1,m} to each other. 
		#This requirement forces m to be even, so that we can write m=2k for some positive integer k.
		#step = 2, let m vary over all possible n−1 choices of even numbers between 1 and 2n
		for i in range(lo + 1, hi + 1, 2):
			if rna[i] == target:
				left = RNASecondaryStructures2(rna, lo + 1, i - 1, dp)
				right = RNASecondaryStructures2(rna, i + 1, hi, dp)
				acc += (left * right) % 1000000
		dp[(lo, hi)] = acc
		return acc

if __name__=='__main__':
	fasta=SeqIO.parse('../rosalind_cat.txt','fasta')
	s=str(list(fasta)[0].seq).upper()
	#RNASecondaryStructures(s)
	print (RNASecondaryStructures2(s, 0, len(s) - 1, {}) % 1000000)
