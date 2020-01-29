a=abs(int(input()))
temp=1
while(a>0):
	temp*=a%10
	a=a//10
print(temp)	