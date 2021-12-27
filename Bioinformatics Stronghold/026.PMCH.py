from Bio import SeqIO
import math

def PerfectMatchingsRNASecondaryStructures(s):
	print(math.factorial(s.count('A'))*math.factorial(s.count('G')))
	return

def totalPerfectMatch(n):
	res=1
	for i in range(1,n+1):
		res=res*((2*i)-1)
	return res

if __name__=='__main__':
	fasta=SeqIO.parse('../rosalind_pmch.txt','fasta')
	s=str(list(fasta)[0].seq).upper()
	PerfectMatchingsRNASecondaryStructures(s)