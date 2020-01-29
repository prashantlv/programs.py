a = int(input("first"))
b = int(input("second"))

if a%b ==0:
	print("{} is divisible by {} ".format(a,b))
else:
	print("reminder of {}/{} is ".format(a,b), a%b)