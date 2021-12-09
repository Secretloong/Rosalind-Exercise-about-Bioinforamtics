
def FindMotifPosition(s,t):
	pos=[]
	for i in range(len(s)-len(t)+1):
		if s[i:i+4] == t:
		#if s[i:].startswith(t): #by Leandro Lima in Rodalind 
			pos.append(str(i+1))
	return pos

if __name__=='__main__':
	s='GATATATGCATATACTT'
	t='ATAT'
	pos=FindMotifPosition(s,t)
	print (' '.join(pos))