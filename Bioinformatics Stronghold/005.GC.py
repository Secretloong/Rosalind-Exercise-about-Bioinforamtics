
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

def ComputingGCContent(fasta):
	gcContent={}
	for i in fasta.keys():
		gcContent[i]=100*(fasta[i].count('G')+fasta[i].count('C'))/len(fasta[i])
	maxID=sorted(fasta.items())[0][0]
	print(maxID)
	print(gcContent[maxID])

if __name__=='__main__':
	fl=open('../test.fa')
	fasta=read_fasta(fl)
	ComputingGCContent(fasta)