#kadane's algorithm

def main():
	arr = [1,2,3,-2,5]
	summ,maxx,l = 0,arr[0],len(arr)

	for i in range(l):
		summ += arr[i]
		if maxx < summ:
			maxx = summ
		if summ < 0:
			summ = 0		
	print(maxx)
if __name__ == '__main__':
	main()
