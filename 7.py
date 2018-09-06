a=255
b=input("Enter the input:")
d=0
if (b<=8):
    c=8-b
    c=2**8-2**c
    print c,".",d,".",d,".",d
elif(b>8 and b<=16):
    c=16-b
    c=2**8-2**c
    print c
    print a,".",c,".",d,".",d
elif(b>16 and b<=24):
    c=24-b
    c=2**8-2**c
    print a,".",a,".",c,".",d
elif(b>24 and b<=32):
    c=32-b
    c=2**8-2**c
    print a,".",a,".",a,".",c
else:
    print "The given number is invalid"
    
