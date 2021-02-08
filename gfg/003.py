
def sort012(arr,n):
    # code here
    a = []
    zero,one,two = 0,0,0
    # for _ in range(n):
    #     a.append(min(arr))
    #     arr.remove(min(arr))
    # arr = a.copy 
#-----------------bcoz no other array has to be used    
    for i in range(n):
        if arr[i] == 0:
            zero += 1
        elif arr[i] == 1:
            one += 1
        else:
            two += 1
    i =0        
    while zero > 0:
        arr[i] = 0
        i += 1
        zero -= 1
    while one > 0:
        arr[i] = 1
        i += 1
        one -= 1
    while two > 0:
        arr[i] = 2
        i += 1
        two -= 1
        
    
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends
