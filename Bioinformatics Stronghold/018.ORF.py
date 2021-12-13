from Bio import SeqIO
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
	#codonsTab={}
	#for i in range(0,len(codons.split()),2):
	#	codonsTab[codons.split()[i]]=codons.split()[i+1]

	codonsTab = dict(zip(codons.split()[::2],codons.split()[1::2])) #by Rayan in Rosalind

	return(codonsTab)

def Complementing(seq):
	seqRC=seq.upper()[::-1].translate(str.maketrans('ACGT', 'TGCA'))
	return (seqRC)

def OpenReadingFrames(seq):
	codonsTab=codonsTable()

	starts=re.finditer(r'(?=ATG)', seq)
	ends=re.finditer(r'(?=TAA)|(?=TAG)|(?=TGA)',seq)
	startsN = [ i.span()[0] for i in starts ]
	endsN = [ i.span()[0] for i in ends]

	frames = []
	for i in startsN:
		for j in range(i,len(seq),3):
			if j in endsN:
				frames.append((i,j))
				break
	results=[]
	for a,b in frames:
		seqPep=''
		for i in range(a,b,3):
			seqPep += codonsTab[seq[i:i+3]]
		results.append(seqPep)
	return(results)

if __name__=='__main__':
	#seqs=SeqIO.parse('../rosalind_orf.txt','fasta')
	seqs=SeqIO.parse('../test.fa','fasta')
	for i in seqs:
		results=OpenReadingFrames(str(i.seq))
		seqRC=Complementing(str(i.seq))
		resultsRC=OpenReadingFrames(seqRC)
		results=set(results).union(set(resultsRC))
		print('\n'.join(list(results)))
