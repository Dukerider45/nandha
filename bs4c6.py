n=raw_input()
m=len(n)
j=0
k=m
for i in range(m):
    p=n[i]
    if((p>='a' and p<='z') or (p>='A' and p<='Z')):
        j=j+1
    try:
        int(p)
    except ValueError:
        k=k-1

m=m-j
j=n.count(' ')
m=m-j
m=m-k
print(m)
    
