a = float(input("side 1: "))
b = float(input("side 2: "))
c = float(input("side 3: "))

if a+b>c and b+c>a and c+a>b:
	print("Feasible")
else:
	print("Not possible")	