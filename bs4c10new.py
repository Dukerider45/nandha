n=int(raw_input())
x=[]
p=1
x.append(str(p))
x.append(str(p))
for i in range(2,n):
    p=int(x[i-2])
    q=int(x[i-1])
    r=p+q
    x.append(str(r))
if(n==1):
    print('1')
else:
    print(' '.join(x))
    
