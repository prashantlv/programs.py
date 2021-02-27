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

