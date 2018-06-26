l=int(input())
n=raw_input()
list=n.split(" ")
q=int(list[0])
for i in range(1,l):
    if(q>int(list[i])):
        q=int(list[i])
print(q)
