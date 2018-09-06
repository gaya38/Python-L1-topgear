def func(a,count):
    for i in a:
        if(i=='e'):
            count=count+1
        else:
            continue
    if(count==2):
        return "TRUE"
    else:
        return "FALSE"
a=raw_input("Enter the string:")
count=0
b=func(a,count)
print b

        
