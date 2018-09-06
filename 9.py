dict1={"Date":["02/15/2016","02/15/2016","01/27/2016","03/31/2016","01/25/2016","02/14/2017","03/15/2016"],"Time":["10:49 PM","10:49 PM","11.46 AM","12.39 PM","10.34 AM","09.13 AM","05.52 PM"],"File Size":[962,943,15,840,2407,0,5],"File Name":["switchfinal.py","switchfinal.py.bak","t.py","t1.py","tc1.py","teat.py","tes.py"]}
l1=dict1.keys()
print l1
a=input("Enter the key number to list the file size:")
b=input("Enter the key number to list the file name:")
l2=dict1[l1[a]]
l3=dict1[l1[b]]
print "The file name which is having 0 bytes:"
for i in range(len(l2)):
    if (l2[i]==0):
        print l3[i]
    else:
        pass

