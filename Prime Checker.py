a=input("enter a num: ")
a=int(a)
for b in range(2,a):
	if a%b==0:
		print("not prime")
		break
else:
	print("prime")