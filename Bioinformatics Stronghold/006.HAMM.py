
def CountingHammingDistance(dna1,dna2):
	alns=[]
	count=0
	alns.append(dna1)
	alns.append(dna2)
	matrix = zip(*alns)
	for i in list(matrix):
		if i[0] != i[1]:
			count+=1
	print(count)


if __name__=='__main__':
	dna1='GAGCCTACTAACGGGAT'
	dna2='CATCGTAATGACGGCCT'
	CountingHammingDistance(dna1,dna2)

	print(sum([a != b for a, b in zip(dna1, dna2)])) #by BF in Rosalind