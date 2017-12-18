n=int(input())
m=0
if n==0:
	m=1
else:
	for i in range (2,n):
		if m==0:
			if n%i==0:
				m=1
if m==1:
	print("the no is not a prime number")
else:
	print("the no is a prime number")