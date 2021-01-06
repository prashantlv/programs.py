def main():
	num,k = map(int, input().split())
	for _ in range(k):
		if num%10==0:
			num=num//10
		else:
			num-=1
	return num

if __name__ == '__main()__':
	print(main())
