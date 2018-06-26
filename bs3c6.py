n=int(input())
p=raw_input()
list=p.split(" ")
a=len(list)
b=a-n
for i in range(b):
    del list[n]
x=[]
for i in range(n):
    m=len(list)
    q=int(list[0])
    for j in range(1,m):
        if(q>int(list[j])):
            q=int(list[j])
    x.append(str(q))
    for j in list:
        if(j==str(q)):
            r=list.index(j)
            del list[r]
print(' '.join(x))
