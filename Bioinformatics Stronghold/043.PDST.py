from Bio import SeqIO
import numpy as np

def hamDis(s1,s2):
	return(sum(a!=b for a,b in zip(s1,s2)))

def CreatingDistanceMatrix(alns):
	dis=np.empty((len(alns),len(alns)))
	for i in range(len(alns)):
		dis[i,i]=0
		for j in range(i+1,len(alns)):
			dis[i,j]=hamDis(alns[i],alns[j])/len(alns[i])
			dis[j,i]=dis[i,j]
	for x in dis:
		print(' '.join([str("%.5f" % y) for y in x]))
	return

if __name__=='__main__':
	fasta=SeqIO.parse('../rosalind_pdst.txt','fasta')
	alns = [str(x.seq) for x in fasta]
	CreatingDistanceMatrix(alns)