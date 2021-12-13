import requests,re
from bs4 import BeautifulSoup

def FindingProteinMotifbyDatabase(url):
	strhtml = requests.get(url)
	soup=BeautifulSoup(strhtml.text,'lxml')
	data=soup.find_all(href=re.compile('Glycosylation'))
	pos=[]
	for item in data:
		num=str(item).rstrip('</a>').split('>')[-1]
		pos.append(num)
	return (pos)

def FindingProteinMotifbyMotif(url):
	strhtml = requests.get(url)
	soup=BeautifulSoup(strhtml.text,'lxml')
	seq=''
	try:
		data=soup.body.strings
		for item in data:
			seq=''.join(item.rstrip().split('\n')[1:])
	except:
		next
	return (seq)


if __name__=='__main__':
	#fl=open('../test.txt')
	fl=open('../rosalind_mprt.txt')
	results={}
	for line in fl:
		url='https://www.uniprot.org/uniprot/'+line.rstrip()+'.fasta'
		seq=FindingProteinMotifbyMotif(url)
		if seq == '':
			continue
		#results[line.rstrip()]=FindingProteinMotifbyDatabase(url)
		
		#(?=...) match the pattern without consume the pattern, so it chould find all overlaping patterns; and (?=...) record the zero position by lookahead assertion, if .?(?=...) may get the 83th character
		for m in re.finditer(r'(?=N[^P][ST][^P])',seq): #[<re.Match object; span=(84, 84), match=''>, <re.Match object; span=(117, 117), match=''>]
		#for m in re.finditer(r'N[^P][ST][^P]',seq): #[<re.Match object; span=(84, 88), match='NFSD'>, <re.Match object; span=(117, 121), match='NSSN'>]
			results.setdefault(line.rstrip(),[]).append(str(m.start()+1))

	for i in results.keys():
		if results[i] != []:
			print(i)
			print(' '.join(results[i]))