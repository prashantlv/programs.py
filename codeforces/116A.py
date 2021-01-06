def main():
	t=int(input())
	temp=0
	current=[]
	for _ in range(t):
		a,b=map(int.input().split())
		temp=temp-(b-a)
		current.append(abs(temp))
	return max(current)
if __name__ == '__main__':
	print(main())
