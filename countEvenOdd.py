a = int(input())
even=0
odd=0
while(a>0):
	b=a%10
	a=a // 10           # // is floor division in py3
	if b%2==0:
		even+=1
	else :
		odd+=1
print("even:{} odd:{}".format(even,odd))