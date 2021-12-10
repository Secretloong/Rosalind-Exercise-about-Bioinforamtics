import numpy as np

def ExpectedOffspring(nums):
	Pr=[1.0,1.0,1.0,0.75,0.5,0]
	print(sum(np.multiply(nums,Pr))*2)

if __name__=='__main__':
	alleNums=[int(x) for x in '1 0 0 1 0 1'.split()]
	ExpectedOffspring(alleNums)
