from math import log10

def RandomStrings(seq, proc):
	#A random string is constructed so that 
	#the probability of choosing each subsequent symbol 
	#is based on a fixed underlying symbol frequency.
	#
	#GC-content offers us natural symbol frequencies 
	#for constructing random DNA strings.
	res=[]
	for p in proc:
		logP=0
		for i in range(len(seq)):
			if seq[i] in 'CG':
				logP=log10(p/2)+logP
			elif seq[i] in 'AT':
				logP=log10((1-p)/2)+logP
			else:
				print ('Wrong with non-ATCG!!!')
		res.append(round(logP,3))
	return(res)

def RandomStrings2(seq, proc): #by Myke in Rosalind
	n = seq.count("G") + seq.count("C")
	return([round((len(seq)-n)*log10(1-gc) + n*log10(gc) - len(seq)*log10(2),3) for gc in proc])

if __name__=='__main__':
	fl=open('../rosalind_prob.txt')
	seq = fl.readline().rstrip().upper()
	proc = [float(x) for x in fl.readline().rstrip().split()]
	#An array B having the same length as A 
	#in which B[k] represents the common logarithm of the probability that a random string 
	#constructed with the GC-content found in A[k] will match s exactly.
	res=[str(x) for x in RandomStrings(seq, proc)]
	print(' '.join(res))
