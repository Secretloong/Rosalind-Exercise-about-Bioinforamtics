from Bio import SeqIO

def recom(seq):
	return (seq[::-1].translate(str.maketrans('ACGT', 'TGCA')))

def countRecom(reads,x):
	res=0
	for s in reads:
		if x == s or recom(x) == s or x == recom(s) or recom(x) == recom(s):
			res+=1
	return (res)

def ErrorCorrectionReads(reads):
	cor=[]
	err=[] # could be replaced by set(reads) - cor
	readNum = dict((x,countRecom(reads,x)) for x in reads)
	for x in readNum.keys():
		if readNum[x] > 1:
			cor.append(x)
		else:
			err.append(x)
	corrected=[]
	for x in err:
		for y in cor:
			if sum(a!=b for a,b in zip(x,y)) == 1:
				corrected.append((x,y))
			elif sum(a!=b for a,b in zip(x,recom(y))) == 1:
				corrected.append((x,recom(y)))
	return (set(corrected))

if __name__=='__main__':
	fasta=SeqIO.parse('../rosalind_corr.txt','fasta')
	reads=[str(x.seq) for x in fasta]
	corrected=ErrorCorrectionReads(reads)
	print('\n'.join(list('->'.join(x) for x in corrected)))