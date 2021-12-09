#######by ye.pandaaaa906 in Rosalind########
from Bio import SeqIO
from itertools import permutations

records = SeqIO.parse('../test.fa', 'fasta')

def is_overlap(record1, record2, o=3):
	return record1.seq.endswith(record2.seq[:o])

print("\n".join((" ".join((record1.id, record2.id)) for record1, record2 in permutations(records, 2) if is_overlap(record1, record2))))

#######self########
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

def OverlapGraphs(fasta):
	sp=list(fasta.keys())
	heads=[fasta.get(x)[:3] for x in sp]
	tails=[fasta.get(x)[-1:-4:-1] for x in sp]
	for i in range(len(sp)):
		for j in range(len(sp)):
			if heads[j] == tails[i] and i != j:
				print (sp[i]+' '+sp[j])

if __name__=='__main__':
	fl=open('../test.fa')
	fasta=read_fasta(fl)
	OverlapGraphs(fasta)