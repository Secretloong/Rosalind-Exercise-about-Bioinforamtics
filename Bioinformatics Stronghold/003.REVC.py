
def Complementing():
	dna='AAAACCCGGT'
	dna=reversed(dna)
	dna2=[]
	for i in dna:
		if i == 'A':
			dna2.append('T')
		elif i == 'T':
			dna2.append('A')
		elif i == 'C':
			dna2.append('G')
		elif i == 'G':
			dna2.append('C')
	print(''.join(dna2))

def Complementing2(): #by Ben Usman in Rosalind
	st = 'AAAACCCGGT'
	st = st.replace('A', 't').replace('T', 'a').replace('C', 'g').replace('G', 'c').upper()[::-1]
	print (st)
	#st[::-1] slicing

def Complementing3(): #by JimHokanson in Rosalind
	s = 'AAAACCCGGT'
	print(s[::-1].translate(str.maketrans('ACGT', 'TGCA')))
	#str.maketrans('ACGT', 'TGCA'): a dictionary mapping Unicode ordinals (integers)
	#s.translate(given translation table)

if __name__=='__main__':
	Complementing()
	Complementing2()
	Complementing3()