a=raw_input()
b=raw_input()
a=a.split(' ')
b=b.split(' ')
c=(int(a[0])*60)+int(a[1])
d=(int(b[0])*60)+int(b[1])
if(c>d):
    n=c-d
else:
    n=d-c
a=str(n/60)
b=str(n%60)
x=[a,b]
print(' '.join(x))
