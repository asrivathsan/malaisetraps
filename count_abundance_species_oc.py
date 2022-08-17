import sys
from collections import Counter
iddict={}

with open(sys.argv[1]) as infile1:
	l=infile1.readlines()
	for each in l:
		m=each.strip().split('\t')
		iddict[m[0]]=m[1]

spcountlist=[]
speccountlist=[]
with open(sys.argv[2]) as infile1:
	l=infile1.readlines()

	for each in l:
		mlist=[]
		m=each.strip().split('\t')
		spec=m[0].strip().split("_")[1]
	#	spec=m[0].strip().split("|")[0]
	#	spec=m[0].strip()
		try:
			spcountlist.append(iddict[spec])
		except KeyError:
			print(spec)
		for spec in m:
			spec=spec.strip().split("_")[1]
	#		spec=spec.strip().split("|")[0]
	#		spec=spec.strip()
			try:
				speccountlist.append(iddict[spec])
			except KeyError:
				pass
speccountdict=Counter(speccountlist)
spcountdict=Counter(spcountlist)

with open(sys.argv[2]+"_speciescounts",'w') as speciesoutfile:
	for each in spcountdict.keys():
		speciesoutfile.write(each+'\t'+str(spcountdict[each])+'\n')


with open(sys.argv[2]+"_specimencounts",'w') as specimenoutfile:
	for each in speccountdict.keys():
		specimenoutfile.write(each+'\t'+str(speccountdict[each])+'\n')

speciesoutfile.close()
specimenoutfile.close()
