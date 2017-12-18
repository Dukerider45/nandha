n=input()
l=len(n)
sum=0
for i in range(0,l):
    x=n[i]
    y=(int(x))**3
    sum +=y
if sum==int(n):
    print("it is an amstrong no")
else:
    print("it is not an amstrong no")
    
