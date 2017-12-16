a=input()
b=input()
c=input()
print("the greatest number is")
if a<b:
	if b<c:
		print(c)
	else:
		print(b)
elif b<c:
	if c<a:
		print(a)
	else:
		print(c)
elif c<a:
	if a<b:
		print(b)
	else:
		print(a)# your code goes here