n=raw_input()
m=len(n)
p=0
q=0
if(n[m-1]=='.'):
    p=1
if(n[0]=='.'):
    q=1
n=n.split('.')
n=len(n)
n=n-p
n=n-q
print(n)
    
