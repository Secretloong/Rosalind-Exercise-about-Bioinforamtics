from itertools import combinations

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

def FindingMotif(fasta):
	motifLen=min([len(fasta.get(x)) for x in fasta.keys()])
	for xlen in range(motifLen,0,-1):
		motifs={}
		for x in fasta.keys():
			for xpos in range(len(fasta[x])-xlen+1):
				motifs.setdefault(x,[]).append(fasta[x][xpos:xpos+xlen])
		
		insec=set(list(motifs.values())[0])
		for a,b in combinations(list(motifs.values()), 2):
			insec.intersection_update(a,b)
		
		xset=[]
		for y in motifs.values():
			xset.extend(y)

		if insec != set():
			xdict=dict((x,xset.count(x)) for x in insec)
			print(xdict)
			print(max(xdict,key = xdict.get))
			break
	return

#########Version edited from Petar Ivanov in Rosalind##########
#########Algorithm: Binary Search, 50 times faster than above##########
def substr_in_all(arr, part):
	for dna in arr:
		if dna.find(part)==-1:
			return False
	return True

def common_substr(arr, l):
	first = arr[0]
	for i in range(len(first)-l+1):
		part = first[i:i+l]
		if substr_in_all(arr, part):
			return part
	return ''

def longest_common_substr(arr):
	l = 0; r = len(arr[0])

	while l+1<r:
		mid = int((l+r) / 2)
		if common_substr(arr, mid)!='':
			l=mid #longer
		else:
			r=mid #shorter
	return common_substr(arr, l)

#########END##########

if __name__=='__main__':
	#fl=open('../test.fa')
	fl=open('../rosalind_lcsm.txt')
	fasta=read_fasta(fl)
	FindingMotif(fasta)

	print(longest_common_substr(list(fasta.values())))