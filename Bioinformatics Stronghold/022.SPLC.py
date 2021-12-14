from Bio import SeqIO
from Bio.Seq import Seq
import re

def codonsTable():
	codons='TTT F      CTT L      ATT I      GTT V \
TTC F      CTC L      ATC I      GTC V \
TTA L      CTA L      ATA I      GTA V \
TTG L      CTG L      ATG M      GTG V \
TCT S      CCT P      ACT T      GCT A \
TCC S      CCC P      ACC T      GCC A \
TCA S      CCA P      ACA T      GCA A \
TCG S      CCG P      ACG T      GCG A \
TAT Y      CAT H      AAT N      GAT D \
TAC Y      CAC H      AAC N      GAC D \
TAA Stop   CAA Q      AAA K      GAA E \
TAG Stop   CAG Q      AAG K      GAG E \
TGT C      CGT R      AGT S      GGT G \
TGC C      CGC R      AGC S      GGC G \
TGA Stop   CGA R      AGA R      GGA G \
TGG W      CGG R      AGG R      GGG G'
	codonsTab = dict(zip(codons.split()[::2],codons.split()[1::2])) #by Rayan in Rosalind
	return(codonsTab)

def RNASplicing(seq,introns):
	codonsTab=codonsTable()
	pattern= '|'.join([i for i in introns])
	patterns=re.compile(pattern)
	newSeq=patterns.sub('',seq)
	print(''.join([codonsTab[newSeq[i:i+3]] for i in range(0,len(newSeq)-3,3)]))
	return

def RNASplicing2(instream): 
	target = str(next(instream).seq) # next() return next/first item in iterator

	for intron in instream:
		target = target.replace(str(intron.seq),"") #I think there could be improved by re.sub(), in case of new seq has replaced pattern

	print (Seq(target).translate()[:-1]) #except for the last codon (Stop)

if __name__=='__main__':
	
	fasta=SeqIO.parse('../rosalind_splc.txt', 'fasta')
	RNASplicing2(fasta) #by sasha in Rosalind

	fasta=SeqIO.parse('../rosalind_splc.txt', 'fasta')
	seq=''
	introns=[]
	for i in fasta:
		if seq == '':
			seq=str(i.seq)
		else:
			introns.append(str(i.seq))
	RNASplicing(seq,introns)
