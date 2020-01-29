a= int(input("Year : "))

if a%4 ==0 and a%400:
	print("Leap Year")
elif a%100!=0:
	print("Usual Year")	
else:
	print("Usual Year")			