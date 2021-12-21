from itertools import combinations

########## first try Brute Force ##########
def check_ordering(seq, l):
	incTag=0
	decTag=0
	inc=()
	dec=()
	for m in range(l+1,2,-1):
		if incTag==1 and decTag==1:
			break
		results=list(combinations([i for i in seq],m))
		for seq0 in results:
			if tuple(sorted(seq0)) == seq0 and incTag == 0:
				inc=tuple(str(i) for i in seq0)
				incTag=1
			if tuple(sorted(seq0,reverse=True)) == seq0 and decTag == 0:
				dec=tuple(str(i) for i in seq0)
				decTag=1
	return (inc,dec)

def LongestIncreasingSubsequence1(pi,n):
	l = 0; r = len(pi)

	inc=()
	dec=()
	while l+1<r:
		mid = int((l+r) / 2)
		(inc,dec)=check_ordering(pi, mid)
		if inc != () or dec != ():
			l=mid #longer
		else:
			r=mid #shorter
	return (inc,dec)

########## second try Dynamic Programming ##########
def wipeCache(old,new,tag):
	for i in old:
		if tag == 1:
			if len(i) < len(new) and new[-1] < i[-1]:
				old.remove(i)
		else:
			if len(i) < len(new) and new[-1] > i[-1]:
				old.remove(i)
	return (old)

def LongestIncreasingSubsequence2(pi,n):
	incDp = []
	incDp.append([pi[0]])
	decDp = []
	decDp.append([pi[0]])
	for i in range(1,n):
		incTag=0
		decTag=0
		incDp0=incDp[:]
		for j in range(len(incDp)):
			if pi[i] > incDp[j][-1]:
				incTag=1
				new=incDp[j][:]
				new.append(pi[i])
				incDp0=wipeCache(incDp0,new,1)
				incDp0.append(new)
		incDp=incDp0[:]
		if incTag == 0:
			incDp.append([pi[i]])

		decDp0=decDp[:]
		for j in range(len(decDp)):
			if pi[i] < decDp[j][-1]:
				decTag=1
				new=decDp[j][:]
				new.append(pi[i])
				decDp0=wipeCache(decDp0,new,0)
				decDp0.append(new)
		decDp=decDp0[:]
		if decTag == 0:
			decDp.append([pi[i]])
	#dict.items() switch to tuples, key gives a function to sort
	#indexSeq = [x[0] for x in sorted(index.items(), key = lambda x:(x[1], x[0]))]
	inc=sorted(incDp, key = lambda x: len(x), reverse=True)[0]
	inc=[str(x) for x in inc]
	dec=sorted(decDp, key = lambda x: len(x), reverse=True)[0]
	dec=[str(x) for x in dec]
	return(inc,dec)

########## third try Arrays and Binary Searching ##########
def long_inc_sseq(seq):
	#https://stackoverflow.com/questions/3992697/longest-increasing-subsequence
	#https://en.wikipedia.org/wiki/Longest_increasing_subsequence
	#Patience Sort

	#loop: 
	#seq: 5, 1, 4, 2, 3
	#ind: 0, 1, 2, 3, 4
	#	L1: Initial, one element, the longest increasing subsequence (length 1)
	#	M [None,0,None,None,None,None]
	#	P [/None(L1 end), None, None, None, None]
	#	L1: seq[1]<seq[0] (1<5), seq[1] could create new longer increasing subsequence (length 1), update
	#	M [None,1,None,None,None,None]
	#	P [/None, /None(L1 end), None, None, None] 
	#	L2: seq[2]<seq[0] && seq[2]>seq[1], With seq[2] and seq[1] we have subsequence of length 2
	#	M [None,1,2,None,None,None]
	#	P [\None, \None, \1(L2 end), None, None]
	#	L2
	#	M [None,1,3,None,None,None]: seq[4]<seq[3] && seq[4]
	#	P [\None, \None, \1, \1(L2 end), None] 
	#	L3
	#	M [None,1,3,4,None,None]
	#	P [\None, \None, \1, \1, \3(L3 end)] 

	n = len(seq)

	#the index of the smallest value, plus 1 to make P[0] available ('None', stop of the reconstruction)
	M = [None] * (n+1)
	#P[i] the index of the predecessor of seq[i] in the longest increasing subsequence ending at seq[i]
	#P is used to build the result at the end.
	P = [None] * n
	#the length of the longest increasing subsequence found up to that moment
	L = 0

	for i in range(0,n):
		#print (i,seq,M,P,L)
		low = 0
		hi = L + 1
		if L == 0: 
			j = 0
		else:
			#Binary search for the largest positive j ≤ L such that X[M[j]] < X[i]
			while low + 1 < hi:
				mid = (hi + low) // 2
				if seq[M[mid]] < seq[i]:
					low = mid
				else:
					hi = mid
		j = low

		#The predecessor of X[i] is the last index of the subsequence of length newL-1
		P[i] = M[j]
		M[j+1] = i
		j=j+1
		#print (i,j-1,j,seq,M,P,L)

		#If we found a subsequence longer than any we've found yet, update L
		if j > L:# or seq[i] < seq[M[j-1]]:
			#M[j+1] = i
			L = j #max(L, j)
		#print(reconsLIS(seq,M,P,L))

	#Reconstruct the longest increasing subsequence
	res = reconsLIS(seq,M,P,L)
	return ([str(i) for i in res[::-1]])

def reconsLIS(seq,M,P,L):
	#Reconstruct the longest increasing subsequence
	res = []
	pos = M[L]
	while L > 0:
		res.append(seq[pos])
		pos = P[pos]
		L -= 1
	return(res)

########## Rosalind ##########
def LongestIncreasingSubsequence3(l,n): #by Andrew in Rosalind, slower than long_inc_sseq()
	inc = [(0,[])]*(n+1) # store the longest sub-l ended by each number in array (index by number value)
	for i in l:
		# the order based on l, than found the largest one which smaller than current element
		#which mean we store the longest sub-l ended by current element in array
		x,y = max(inc[:i])
		# the length plus 1, the sub-l append current element
		inc[i] = (x+1,y+[i])
	return (list(map(str,max(inc)[1])))

def LongestIncreasingSubsequence4(l, n): #by dnanag in Rosalind, slower than long_inc_sseq()
	#used max(,key=len) to displace the record or length od sub-l
	inc = [[]]*(n+1)
	for i in l:
		inc[i] = max(inc[:i], key=len)+[i]
	return (list(map(str, max(inc, key=len))))

if __name__=='__main__':
	fl = open('../test.txt') #rosalind_lgis
	files=fl.readlines()
	n = int(files[0].rstrip())
	pi = [int(i) for i in files[1].rstrip().split()]
	#print(n, pi)
	#(inc,dec)=LongestIncreasingSubsequence1(pi,n)
	
	inc = long_inc_sseq(pi)
	inc3=LongestIncreasingSubsequence3(pi,n)
	inc4=LongestIncreasingSubsequence4(pi,n)
	pi.reverse()
	dec = long_inc_sseq(pi)
	dec3=LongestIncreasingSubsequence3(pi,n)
	dec4=LongestIncreasingSubsequence4(pi,n)
	dec.reverse()
	dec3.reverse()
	dec4.reverse()

	print(' '.join(inc))
	print(' '.join(dec))
	print(' '.join(inc3)+'\n'+' '.join(dec3))
	print(' '.join(inc4)+'\n'+' '.join(dec4))
