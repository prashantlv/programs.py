from math import *

num = int(input("Enter number: "))
def isPrime(a):
	if a<2 or a==4:                   # sqrt(4)=2 and i<2 will be false
		return print("Not a Prime number")
	elif a==2:
		return print("Prime number")
	limit = sqrt(a)
	i=2
	while i<limit:
		if a%i ==0:
			return print("Not a Prime number")
		i+=1
	return print("Prime number")		
isPrime(num)	