def RNA2Protein(rna):
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

	traL =  codons.split() #by Ben Usman in Rosalind
	traDict = dict(zip(traL[0::2], traL[1::2])) #by Ben Usman in Rosalind

	protein=''
	for i in range(0,len(rna),3):
		j=i+3
		if codonTab[rna[i:j]] != 'Stop':
			#protein+=codonTab[rna[i:j]]
			protein+=traDict[rna[i:j]]
	print(protein)

if __name__=='__main__':
	rna='AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'
	RNA2Protein(rna)