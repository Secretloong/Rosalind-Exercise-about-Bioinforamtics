from functools import reduce

def codonsTable():
	codonTab={}
	codons='UUU F      CUU L      AUU I      GUU V \
			UUC F      CUC L      AUC I      GUC V \
			UUA L      CUA L      AUA I      GUA V \
			UUG L      CUG L      AUG M      GUG V \
			UCU S      CCU P      ACU T      GCU A \
			UCC S      CCC P      ACC T      GCC A \
			UCA S      CCA P      ACA T      GCA A \
			UCG S      CCG P      ACG T      GCG A \
			UAU Y      CAU H      AAU N      GAU D \
			UAC Y      CAC H      AAC N      GAC D \
			UAA Stop   CAA Q      AAA K      GAA E \
			UAG Stop   CAG Q      AAG K      GAG E \
			UGU C      CGU R      AGU S      GGU G \
			UGC C      CGC R      AGC S      GGC G \
			UGA Stop   CGA R      AGA R      GGA G \
			UGG W      CGG R      AGG R      GGG G'
	for i in range(0,len(codons.split()),2):
		codonTab[codons.split()[i]] = codons.split()[i+1]
	codonTab = dict((i,list(codonTab.values()).count(i)) for i in codonTab.values())
	print
	return(codonTab)

def InferringmRNAfromProtein(protein):
	codonTab=codonsTable()
	totalCand=1
	for i in range(len(protein)):
		totalCand = totalCand * codonTab[protein[i]]
	result=totalCand*codonTab['Stop'] % 1000000
	return(result)

def InferringmRNAfromProtein2(protein): #if you want to know modulo, please modulo 1M every step (a*1M+n)*b = (a*b*1M)+b*n
	codonTab=codonsTable()
	totalCand=[]
	for i in range(len(protein)):
		totalCand.append(codonTab[protein[i]])
	totalCand.append(codonTab['Stop'])
	result = reduce(lambda x, y: x*y % 1000000, totalCand)
	return (result)

if __name__=='__main__':
	fl=open('../rosalind_mrna.txt')
	protein=fl.read().rstrip()
	mod1M=InferringmRNAfromProtein(protein)
	print(mod1M)
	mod1M=InferringmRNAfromProtein2(protein)
	print(mod1M)