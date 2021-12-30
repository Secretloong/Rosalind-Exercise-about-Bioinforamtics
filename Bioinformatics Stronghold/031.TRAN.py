from Bio import SeqIO

def Transitions2Transversions(s1,s2):
	profiles=list(zip(s1,s2))
	transi=0
	transv=0
	for i in profiles:
		if i[0] == i[1]:
			continue
		elif set(i) == {'A','G'} or set(i) == {'C','T'}:
			transi+=1
		else:
			transv+=1
	R=transi/transv
	print (R)
	return

if __name__=='__main__':
	fasta=list(SeqIO.parse('../rosalind_tran.txt','fasta'))
	s1=str(fasta[0].seq)
	s2=str(fasta[1].seq)
	Transitions2Transversions(s1,s2)