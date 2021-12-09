
def read_fasta(fl):
	fasta={}
	chrID=''
	for line in fl:
		if line.startswith('>'):
			chrID=line.replace('>','').rstrip()
		else:
			if chrID in fasta.keys():
				fasta[chrID]=fasta[chrID]+line.rstrip().upper()
			else:
				fasta[chrID]=line.rstrip().upper()
	return(fasta)

def ConsensusProfile(fasta):
	sp=fasta.keys()
	strands=[fasta.get(x) for x in sp]
	matrix=zip(*strands)
	profile_matrix = list(map(lambda x: [x.count(base) for base in 'ACGT'], matrix))
	conSeq=''
	for i in profile_matrix:
		for j in range(4):
			if i[j]==max(i):
				conSeq=conSeq+'ACGT'[j]
	print (conSeq)
	profile_matrix_t=list(zip(*profile_matrix))
	for i in range(4):
		print ('ACGT'[i]+': '+' '.join([str(x) for x in profile_matrix_t[i]]))

def ConsensusProfile2(f):
	strands = [x.strip() for x in f.readlines()]
	matrix = zip(*strands)
	profile_matrix = map(lambda x: dict((base, x.count(base)) for base in 'ACGT'), matrix)
	consensus = [max(x,key = x.get) for x in profile_matrix]
	print (''.join(consensus))

if __name__=='__main__':
	fl=open('../test.fa')
	fasta=read_fasta(fl)
	ConsensusProfile(fasta)
	fl.close()

	fl=open('../test.fa')
	ConsensusProfile2(fl) #by Darkstar in Rosalind
	fl.close()