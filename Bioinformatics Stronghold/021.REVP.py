from Bio import SeqIO

def revComp(seq):
	seqRC=seq[::-1].translate(str.maketrans('ATCG','TAGC'))
	return(seqRC)

def LocatingRestrictionSites(seq):
	for l in range(4,13,2):
		for i in range(len(seq)):
			if i+l<=len(seq) and seq[i:i+l] == revComp(seq[i:i+l]):
				print (i+1,l)
	return

if __name__=='__main__':
	fasta=SeqIO.parse('../rosalind_revp.txt','fasta')
	for seq in fasta:
		LocatingRestrictionSites(str(seq.seq))
