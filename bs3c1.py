p=raw_input()
list=p.split(' ')
n=int(list[0])
a=int(list[1])
d=int(list[2])
an=a+(n-1)*d
s=n*(a+an)/2
print(s)
