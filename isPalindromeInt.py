num = int(input())
sum=0
a= num
while(a>0):
	r=a%10
	sum=sum*10+r
	a=a//10
if sum == num:
	print("Palindrome")
else:
	print("Not a Palindrome")			