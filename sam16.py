print("enter the starting on:")
p=int(input())
print("enter the ending on:")
q=int(input())
for n in range(p+1,q):
    m=0
    if n==0:
            m=1
    else:
            for i in range (2,n):
                    if m==0:
                            if n%i==0:
                                    m=1
    if m==0:
            print(n)
