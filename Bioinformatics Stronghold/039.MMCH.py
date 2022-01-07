from Bio import SeqIO
from math import factorial
from functools import reduce

def MaximumMatchingsRNASecondaryStructures(seq):
	m1=min(seq.count('A'),seq.count('U'))
	n1=max(seq.count('A'),seq.count('U'))
	m2=min(seq.count('C'),seq.count('G'))
	n2=max(seq.count('C'),seq.count('G'))
	#print (m1,n1,m2,n2)
	dp = 1
	for i in range(m1):
		dp = dp * (n1-i)
	for i in range(m2):
		dp = dp * (n2-i)
	print (dp)
	return

def MaximumMatchingsRNASecondaryStructures2(s): #by Tom C in Rosalind
	##sorted to min & max
	a, b = sorted([seq.count("G"), seq.count("C")])
	c, d = sorted([seq.count("A"), seq.count("U")])

	#reduce: apply a particular function passed in its argument to all of the list elements, the result passed to next running of function
	m = lambda x,y: x*y
	print(reduce(m, range(b - a + 1, b + 1)) * reduce(m, range(d - c + 1, d + 1)))
	return

if __name__=='__main__':
	fasta=SeqIO.parse('../rosalind_mmch.txt','fasta')
	seq=str(list(fasta)[0].seq)
	#print(seq)
	MaximumMatchingsRNASecondaryStructures(seq)
	MaximumMatchingsRNASecondaryStructures2(seq)