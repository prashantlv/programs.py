def doUnion(a,n,b,m):
	return len(set(a+b))
#========================

#User function Template for python3

class Solution:
    #Function to return the count of number of elements in union of two arrays.
        #code here
    def doUnion(self,a,n,b,m):
        arr = []
        arr = a
        for i in range(len(b)):
            if b[i] not in arr:
                arr.append(b[i])
        return len(set(arr))

#{
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__=='__main__':
    t=int(input())
    for _ in range(t):

        n,m=[int(x) for x in input().strip().split()]

        a=[int(x) for x in input().strip().split()]
        b=[int(x) for x in input().strip().split()]
        ob=Solution()

        print(ob.doUnion(a,n,b,m))
# } Driver Code Ends
