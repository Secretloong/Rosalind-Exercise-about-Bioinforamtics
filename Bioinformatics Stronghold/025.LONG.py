from Bio import SeqIO
from itertools import permutations

########## first try based on graph ##########
def common_substr(seq1, seq2, l):
	for i in range(len(seq2)-l+1):
		part = seq2[i:i+l]
		if seq1.endswith(part):
			return part
	return ''

def is_overlap(seq1, seq2):
	o=int(len(seq2)/2)
	
	l = 0; r = len(seq2)
	while l+1 < r:
		mid = int((l+r)/2)
		if common_substr(seq1, seq2, mid)!='':
			l=mid #longer
		else:
			r=mid #shorter

	if len(common_substr(seq1, seq2, l)) >= len(seq1)/2 and len(common_substr(seq1, seq2, l)) >= len(seq2)/2:
		return True
	return False

def connect_strings(seq1,seq2):
	l = 0; r = len(seq2)
	while l+1 < r:
		mid = int((l+r)/2)
		if common_substr(seq1, seq2, mid)!='':
			l=mid #longer
		else:
			r=mid #shorter
	return(seq1+seq2[l:])

########## https://github.com/mtarbit/Rosalind-Problems/blob/master/e025-long.py ##########
def find_overlaps(arr, acc=''):
	if len(arr) == 0:
		return acc

	elif len(acc) == 0:
		acc = arr.pop(0)
		return find_overlaps(arr, acc)

	else:
		for i in range(len(arr)):
			a = arr[i]
			l = len(a)

			for p in range(l // 2):
				q = l - p

				if acc.startswith(a[p:]):
					arr.pop(i)
					return find_overlaps(arr, a[:p] + acc)

				if acc.endswith(a[:q]):
					arr.pop(i)
					return find_overlaps(arr, acc + a[q:])

########## by Rayan in Rosalind ##########
def revcomp(s): #make sure two directs could be connected
	return s[::-1].translate(str.maketrans('ACGT', 'TGCA'))

def overlap(a,b): #from 1/2 length to whole length to find the longest overlapped reads, there is only one direct
	candidates_overlaps = [l for l in range(min(len(a),len(b))//2, min(len(a),len(b))) if a[-l:] == b[:l]]
	return max(candidates_overlaps) if len(candidates_overlaps)>0 else 0

def extend(consensus,remaining_reads):
	while len(remaining_reads)>0:
		overlap_length, best_overlap = max( [(overlap(consensus,b), b) for b in remaining_reads], key = lambda x: x[0] )
		if overlap_length == 0:
			break
		remaining_reads.remove(best_overlap)
		consensus += best_overlap[overlap_length:]
	return consensus

##########################################

if __name__=='__main__':
	fasta=SeqIO.to_dict(SeqIO.parse('../rosalind_long.txt','fasta'))
	
	########## the slowest, 3 times than others
	graphPairs={}
	for record1, record2 in permutations(fasta.keys(), 2):
		if is_overlap(str(fasta[record1].seq), str(fasta[record2].seq)):
			graphPairs[record1]=[record2]
	for i in graphPairs.keys():
		for j in graphPairs.keys():
			if i==graphPairs[j][-1]:
				graphPairs[j].extend(graphPairs[i])
	bestGraph=max(graphPairs.items(),key=lambda item: len(item[1])) #please notice the lambda, not the key=len, that's wrong
	bestGraph=bestGraph[0]+' '+' '.join(bestGraph[1])
	bestGraph=bestGraph.split()
	bestStrings=[fasta[x].seq for x in bestGraph]
	for i in range(len(bestStrings)-1):
		bestStrings[i+1]=connect_strings(bestStrings[i],bestStrings[i+1])
	print (bestGraph)
	print (bestStrings[-1])
	print ()
	
	########## the fastest
	large_dataset=[str(fasta[x].seq) for x in fasta.keys()]
	print (find_overlaps(large_dataset))
	print ()
	
	########## the faster
	s=[str(fasta[x].seq) for x in fasta.keys()]
	print (revcomp(extend(revcomp(s[0]), list(map(revcomp,s[1:]))))[:-len(s[0])] + extend(s[0], s[1:]))
	