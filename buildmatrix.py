import sys,os
taxlist=[]
alltaxlist=[]
with open(sys.argv[2]) as infile:
    l=infile.readlines()
    for each in l:
        taxlist.append(each.strip())
dirlist=os.listdir(sys.argv[1])
totals={}
specieslist=[]
specieslist_all=[]
indicts={}
indicts_all={}
filelist=[]
for fname in dirlist:
    filelist.append(fname)
    eachdict={}
    with open(sys.argv[1]+"/"+fname) as infile:
        l=infile.readlines()
        for each in l:
            m=each.strip().split('\t')
            eachdict[m[0]]=m[1]
            if m[0] in taxlist:
                try:
                    totals[fname]+=int(m[1])
                except KeyError:
                    totals[fname]=int(m[1])
            if m[0] not in specieslist:
                if m[0] in taxlist:
                    specieslist.append(m[0])
            if m[0] not in specieslist_all:
                specieslist_all.append(m[0])
                    
    indicts[fname]=eachdict
speciesdict={}
for each in specieslist:
    eachlist=[]
    for f in filelist:
        try:
            eachlist.append(float(indicts[f][each])/float(totals[f]*100))
        except KeyError:
            eachlist.append(0)
    speciesdict[each]=sum(eachlist)/len(eachlist)



filelist.sort()
with open(sys.argv[3]+"chosen_prop",'w') as outfile1:
    with open(sys.argv[3]+"_chosen_abs",'w') as outfile2:
        with open(sys.argv[3]+"_all",'w') as outfile3:
            outfile1.write("Taxon")
            outfile2.write("Taxon")
            outfile3.write("Taxon")
            for each in filelist:
                outfile1.write("\t"+each)
                outfile2.write("\t"+each)
                outfile3.write("\t"+each)
            outfile1.write('\n')
            outfile1.write("Total Species")

            outfile2.write('\n')
            outfile2.write("Total Species")
            outfile3.write('\n')
            for each in filelist:
                outfile1.write("\t"+str(totals[each]))
                outfile2.write("\t"+str(totals[each]))
            outfile1.write('\n')
            outfile2.write('\n')
            for each in dict(sorted(speciesdict.items(), key=lambda item: item[1], reverse=True)).keys():
                outfile1.write(each)
                outfile2.write(each)

                for f in filelist:
                    try:
                        outfile1.write("\t"+str(float(indicts[f][each])/float(totals[f])*100))
                        outfile2.write("\t"+str(indicts[f][each]))

                    except KeyError:
                        outfile1.write("\t0")
                        outfile2.write("\t0")
                outfile1.write('\n')
                outfile2.write('\n')
            for each in specieslist_all:
                outfile3.write(each)
                for f in filelist:
                    try:
                        outfile3.write("\t"+str(indicts[f][each]))

                    except KeyError:
                        outfile3.write("\t0")
                outfile3.write('\n')
