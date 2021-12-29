from Bio import SeqIO
import re

def FindingSplicedMotif(s,t):
	patterns=''
	res=[]

	init = re.search(t[0],s).span()[1]
	lastPos = init
	res.append(init)
	
	for i in range(1,len(t)):
		patterns = t[i-1] + '.*?' + t[i]
		res0 = re.search(patterns,s[lastPos-1:])
		res.append(res0.end()+lastPos-1)
		lastPos=res0.end()+lastPos-1
	return res

def FindingSplicedMotif2(s,t): #by Rayan in Rosalind
	res=[]
	i = 0
	for c in t:
		i = (i + s[i:].index(c)) + 1
		res.append(str(i))
	return res

if __name__=='__main__':
	fasta=list(SeqIO.parse('../rosalind_sseq.txt','fasta'))
	s=str(fasta[0].seq)
	t=str(fasta[1].seq)
	#print (s,t)
	res=[str(x) for x in FindingSplicedMotif(s,t)]
	print(' '.join(res))

	res=FindingSplicedMotif2(s,t)
	print(' '.join(res))
