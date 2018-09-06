lst=[]
lst2=[]
lst3=[]
n=input("Enter the list length:")
for i in range(n):
    a=input("Enter the list elements:")
    lst.append(a)
print "The list:",lst
print "The list after removing the duplicates:"
for i in range(n):
    cnt=0
    for j in range(n):
        if(lst[i]==lst[j]):
            cnt=cnt+1
        else:
            pass
    if(cnt>1 and lst[i] not in lst2):
        lst2.append(lst[i])
    elif(lst[i] not in lst2):
        lst3.append(lst[i])
    else:
        pass
lst=lst2+lst3
print lst
        
