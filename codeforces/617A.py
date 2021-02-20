def main(a):
	arr=[5,4,3,2,1]
	count = 0
	for i in arr:
		if a >= i:
			count = count + a // i
			a = a%i
	print(count)		

if __name__ == '__main__':
	x = int(input())
	main(x)

