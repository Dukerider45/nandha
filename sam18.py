print("enter the starting no:")
p=int(input())
print("enter the ending no:")
q=int(input())
for m in range(p+1,q):
    n=str(m)
    l=len(n)
    sum=0
    for i in range(0,l):
        x=n[i]
        y=(int(x))**3
        sum +=y
    if sum==int(n):
        print(n)
    
    
