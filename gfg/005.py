
#code without algo---------------
def main():
	arr = list(map(int, input().split()))
    a=[]
    for i in range(len(arr)):
       if arr[i] < 0:
           a.insert(1, arr[i])
       else:
           a.insert(len(a), arr[i])
    print(a)
#quick sort-------------------	
	temp=None
	j=0
	for i in range(len(arr)):
		if arr[i] < 0:
			temp = arr[i]
			arr[i]=arr[j]
			arr[j]=temp
			j += 1
	print(arr)		        

if __name__ == '__main__':
	main()
