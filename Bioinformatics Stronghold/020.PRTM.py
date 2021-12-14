
def weight():
	#the monoisotopic mass of water is considered to be 18.01056 Da
	mass='A   71.03711 \
C   103.00919 \
D   115.02694 \
E   129.04259 \
F   147.06841 \
G   57.02146 \
H   137.05891 \
I   113.08406 \
K   128.09496 \
L   113.08406 \
M   131.04049 \
N   114.04293 \
P   97.05276 \
Q   128.05858 \
R   156.10111 \
S   87.03203 \
T   101.04768 \
V   99.06841 \
W   186.07931 \
Y   163.06333'
	massTab=dict(zip(mass.split()[::2],mass.split()[1::2]))
	
	massTab=dict(zip(mass.split()[::2],map(float,mass.split()[1::2]))) #could use map() in zip()
	return (massTab)

def CalculatingProteinMass(seq):
	massTab = weight()
	weightPro = [massTab[seq[i]] for i in range(len(seq))]
	#weightPro.append('18.01056')
	#print(round(sum(float(i) for i in weightPro),3))

	print("%.3f" %(sum(map(lambda x:massTab[x],seq)))) #by Rayan in Rosalind

	return

if __name__=='__main__':
	fl=open('../rosalind_prtm.txt')
	seq=fl.read().replace('\n','')
	CalculatingProteinMass(seq)