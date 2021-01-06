def main():
	c,d,n=map(int,input().split())
	cost=[i*c for i in range(1,n+1)]
	if sum(cost) <= d:
		return 0
	else:
		return sum(cost)-d
if __name__ == '__main__':
	print(main())
