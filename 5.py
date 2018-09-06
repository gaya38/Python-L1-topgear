r=open("input.txt","r")
a=r.readlines()
w=open("output.txt","w")
w.write("s.no  chars  words\n")
for i in range(len(a)):
    k=0
    cntw=1
    cntc=-1
    for j in a[i]:
        if (j==" "):
            cntw=cntw+1
        else:
            cntc=cntc+1
    print cntw,cntc
    cntc=str(cntc)
    k=i+1
    k=str(k)
    w.write(k)
    w.write("\t")
    w.write(cntc)
    w.write("\t")
    cntw=str(cntw)
    w.write(cntw)
    w.write("\n")
r.close()
w.close()

    
