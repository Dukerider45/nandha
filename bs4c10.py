n=int(raw_input())
x=[]
p=1
x.append(str(p))
x.append(str(p))
for i in range(n-2):
    p=int(x[i])
    q=int(x[i+1])
    r=p+q
    x.append(str(r))
print(' '.join(x))
    
