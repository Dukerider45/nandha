n=raw_input()
n=n.split(' ')
m=len(n)
p=int(n[0])
for i in range (1,m):
    q=int(n[i])
    if(p<q):
        p=int(n[i])
print(p)
