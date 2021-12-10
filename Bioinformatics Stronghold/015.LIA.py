from itertools import product,combinations
from scipy.stats import binom
import matplotlib.pyplot as plt
import numpy as np

def IndependentAssortment(k,n):
	#donot multiply the former generation probability, here is the expansion equation but is too slow for n>5
	print (1-sum(((3/4)**(2**k-x))*((1/4)**x)*len(list(combinations(list(range(2**k)),x))) for x in range(n)))

	#they are also binomial distribution
	#minus Cumulative Distribution Function of n-1, get Cumulative Distribution Function of at least n 
	print(1-binom.cdf(n-1, 2**k, 0.25))
	
	###visualizing
#	fig,ax = plt.subplots(1,1)
#	x = np.arange(binom.ppf(0.01, 2**k, 0.25),binom.ppf(0.99, 2**k, 0.25))
#	ax.plot(x, binom.pmf(x, 2**k, 0.25),'o')
#	plt.show()

if __name__=='__main__':
	IndependentAssortment(2,1)
	#IndependentAssortment(6,16)

	###list the allel table
#	crossing = list(product('Aa', 'Bb', repeat=2))
#	print(crossing)
#	print ([''.join(sorted(x, key=lambda x: x.lower())) for x in crossing])