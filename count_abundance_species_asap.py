import sys
from collections import Counter
iddict={}

with open(sys.argv[1]) as infile1:
	l=infile1.readlines()
	for each in l:
		m=each.replace("-","_").strip().split('\t')
		iddict[m[0]]=m[1]

icount=0
splist1={}
splist2={}
splist3={}
speccountlist=[]
with open(sys.argv[2]) as infile1:
	l=infile1.readlines()
	scoredict={}
	m=l[8].strip().split("]")[0].split("[")[1].split("/")
	m=[x.strip() for x in m]
	m=[float(x) for x in m]
	m1=l[8].strip().split("]")[0].split("[")[1].split("/")
	m1=[x.strip() for x in m1]
	m1=[float(x) for x in m1]
	cols=[]
	m.sort()
	for i,each in enumerate(m1):
		if each == m[0]:
			if len(cols)<3:
				if i not in cols:
					cols.append(i)
					break
			else:
				break
	for i,each in enumerate(m1):			
		if each == m[1]:
			if len(cols)<3:
				if i not in cols:
					cols.append(i)
					break
			else:
				break
	for i,each in enumerate(m1):	
		if each == m[2]:
			if len(cols)<3:
				if i not in cols:
					cols.append(i)
					break
			else:
				break
	print(l[8],cols)
	for i,j in enumerate(l[11:]):
		try:
			m1=j.strip().replace(";","").split(":")[1].split("/")
			m1=[x.strip() for x in m1]
			m1=[int(x) for x in m1]
			spec=j.strip().split(":")[0].strip()
		#	spec=j.strip().split(":")[0].strip().split("_")[1]
		#	spec=j.strip().split(":")[0].strip().split("_")[0]+"_"+j.strip().split(":")[0].strip().split("_")[1]
		#	spec=j.strip().split(":")[0].strip().split("_")[2]+"_"+j.strip().split(":")[0].strip().split("_")[3]
			try:
				speccountlist.append(iddict[spec])
				splist1[m1[cols[0]]]=iddict[spec]
				splist2[m1[cols[1]]]=iddict[spec]
				splist3[m1[cols[2]]]=iddict[spec]
			except KeyError:
				print(spec)
		except IndexError:
			pass

speccountdict=Counter(speccountlist)
spcountdict1=Counter(splist1.values())
spcountdict2=Counter(splist2.values())
spcountdict3=Counter(splist3.values())

speciesoutfile1=open(sys.argv[2]+"_speciescounts1",'w')
speciesoutfile2=open(sys.argv[2]+"_speciescounts2",'w')
speciesoutfile3=open(sys.argv[2]+"_speciescounts3",'w')
specimenoutfile=open(sys.argv[2]+"_specimencounts",'w')
for each in spcountdict1.keys():
	speciesoutfile1.write(each+'\t'+str(spcountdict1[each])+'\n')
for each in spcountdict2.keys():
	speciesoutfile2.write(each+'\t'+str(spcountdict2[each])+'\n')
for each in spcountdict3.keys():
	speciesoutfile3.write(each+'\t'+str(spcountdict3[each])+'\n')	
for each in speccountdict.keys():
	specimenoutfile.write(each+'\t'+str(speccountdict[each])+'\n')

speciesoutfile1.close()
speciesoutfile2.close()
speciesoutfile3.close()
specimenoutfile.close()
