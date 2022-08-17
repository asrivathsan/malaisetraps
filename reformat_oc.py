import sys

with open(sys.argv[1]) as infile:
	l=infile.readlines()
	for each in l:
		m=each.strip().split("]")
		perc=each.split(" ")[0]
		if float(perc)<=5.0:
			with open(sys.argv[1]+"_byid"+perc,'w') as outfile:
				for c in m:
					try:
						c=c.split("[")[1]
						outfile.write(c.replace(",","\t").replace("'","")+'\n')
					except:
						pass
