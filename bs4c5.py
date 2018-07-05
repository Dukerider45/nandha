n=raw_input()
m=len(n)
j=m
for i in range (m):
    try:
        int(n[i])
    except ValueError:
        j=j-1
print(j)
