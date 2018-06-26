n=int(input())
p=raw_input()
list=p.split(" ")
q=len(list)
m=q-n
if(m<0):
    print('invalid data')
elif(m>0):
    for i in range(m):
        del list[n]
        for i in range(n):
            x=[]
            a=list[i]
            x.append(a)
            x.append(str(i))
            print(' '.join(x))
else:
    for i in range(n):
        x=[]
        a=list[i]
        x.append(a)
        x.append(str(i))
        print(' '.join(x))

