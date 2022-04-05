n=10
a=0
b=1
count =0
if(n<=0):
    print(a)
elif(n==1):
    print(b)
else:
    while(count < n):
        print(a)
        m = a+b 
        a = b
        b = m 
        count += 1