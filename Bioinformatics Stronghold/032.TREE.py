
def CompletingTree(n,edges):
	#all clusters numbers minus 1
	clus=['None']*n
	tag=0
	for i in range(1,n+1):
		for x in edges:
			if i in x:
				if clus[x[1]-1] == 'None' and clus[x[0]-1] == 'None':
					tag+=1
					clus[x[1]-1]=tag
					clus[x[0]-1]=tag
				elif clus[x[1]-1] != 'None':
					clus[x[0]-1]=clus[x[1]-1]
				elif clus[x[0]-1] != 'None':
					clus[x[1]-1]=clus[x[0]-1]
	for i in range(len(clus)):
		if clus[i] == 'None':
			tag+=1
	print (tag-1)

def CompletingTree2(n,edges):
	#Tree has One Less Edge than it has Nodes: (n-1)-m, n: nodes Num, m: edge Num
	print(n-1-len(edges))

if __name__=='__main__':
	fl=open('../rosalind_tree.txt')
	n=int(fl.readline().rstrip())
	edges=[list(int(x) for x in line.rstrip().split()) for line in fl]
	CompletingTree(n,edges)
	CompletingTree2(n,edges)