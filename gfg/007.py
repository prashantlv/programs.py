#approach 01 with pop()


def rotate( arr, n):
    for i in range(1):
        arr.insert(0,arr.pop())
    return arr    
 
def main():

	N = int(input())
	A = map(int, input().split())
	A = list(A)
	print(rotate(A,N))

if __name__ == '__main__':
	main()	
#----------------------------------------
#approach 02 with iteration / another array
def main(arr,k):
	a,l = [], len(arr)
	a = arr[-k:l]
	a += arr[0:l-k]
	print(a)

if __name__ == '__main__':
	arr = map(int, input().split())
	k = int(input())
	main(list(arr),k)

