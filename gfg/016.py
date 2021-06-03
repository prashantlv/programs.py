#Naive approach
class Solution:
    #User function Template for python3
    
    # arr[]: Input Array
    # N : Size of the Array arr[]
    #Function to count inversions in the array.
    def inversionCount(self, arr, n):
        # Your Code Here
        a = 0
        for i in range(n):
            for j in range(i+1,n):
                if (arr[i] > arr[j]):
                    a += 1
        return a 

##############################333333


class Solution:
    #Back-end complete function Template for Python 3

    #global variable to count total inversions
    inversion_count=0

    #Function to count inversions in the array.
    def inversionCount(self, a,n):
        global inversion_count
        inversion_count = 0
        self.merge_sort(a, 0, n - 1)
        #returning the count of inversions in the array.
        return inversion_count

    #Function to sort and merge two parts of array.
    def merge(self, a, start, mid, end):
        global inversion_count
        temp = [0 for i in range(end - start + 1)]

        #i is pointer for left subarray.
        #j is pointer for right subarray.
        #k is index for resultant merged subarray.
        i, j, k = start, mid + 1, 0

        #Using two pointers over the array which helps in storing the
        #smaller element and thus merging the subarray.
        while (i <= mid and j <= end):

            #Comparing element of the array at pointers i and j and accordingly
            #storing the smaller element and updating the pointers.
            if (a[i] <= a[j]):
                temp[k] = a[i]
                k += 1
                i += 1
            else:
                temp[k] = a[j]
                k += 1
                j += 1
                #Adding the inversions which is the number of elements which
                #are smaller than arr[j] in the left half of the array.
                inversion_count += mid - i + 1

      #Copying the remaining elements of left subarray(if there are any)to temp.
        while (i <= mid):
            temp[k] = a[i]
            k += 1
            i += 1

      #Copying the remaining elements of right subarray(if there are any)to temp.
        while (j <= end):
            temp[k] = a[j]
            k += 1
            j += 1

        #Copying back the merged elements to original array.
        for i in range(start, end + 1):
            a[i] = temp[i - start]

    #Function to mergesort the array, which uses divide and conquer algorithm
    #on left and right halves of array for mergesort operation.
    def merge_sort(self, a,start,end):

        if (start < end):

            mid = (start + end) // 2
            #Calling recursive function to sort left half of the array.
            self.merge_sort(a, start, mid)

            #Calling recursive function to sort right half of the array.
            self.merge_sort(a, mid + 1, end)

            #Calling merge function which sorts and merges both halves
            #of the array obtained after calling both recursive function.
            self.merge(a, start, mid, end)

############################################################



# Python 3 program to count inversions in an array

# Function to Use Inversion Count
def mergeSort(arr, n):
    # A temp_arr is created to store
    # sorted array in merge function
    temp_arr = [0]*n
    return _mergeSort(arr, temp_arr, 0, n-1)

# This Function will use MergeSort to count inversions

def _mergeSort(arr, temp_arr, left, right):

    # A variable inv_count is used to store
    # inversion counts in each recursive call

    inv_count = 0

    # We will make a recursive call if and only if
    # we have more than one elements

    if left < right:

        # mid is calculated to divide the array into two subarrays
        # Floor division is must in case of python

        mid = (left + right)//2

        # It will calculate inversion
        # counts in the left subarray

        inv_count += _mergeSort(arr, temp_arr,
                                    left, mid)

        # It will calculate inversion
        # counts in right subarray

        inv_count += _mergeSort(arr, temp_arr,
                                  mid + 1, right)

        # It will merge two subarrays in
        # a sorted subarray

        inv_count += merge(arr, temp_arr, left, mid, right)
    return inv_count

# This function will merge two subarrays
# in a single sorted subarray
def merge(arr, temp_arr, left, mid, right):
    i = left     # Starting index of left subarray
    j = mid + 1 # Starting index of right subarray
    k = left     # Starting index of to be sorted subarray
    inv_count = 0

    # Conditions are checked to make sure that
    # i and j don't exceed their
    # subarray limits.

    while i <= mid and j <= right:

        # There will be no inversion if arr[i] <= arr[j]

        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            k += 1
            i += 1
        else:
            # Inversion will occur.
            temp_arr[k] = arr[j]
            inv_count += (mid-i + 1)
            k += 1
            j += 1

    # Copy the remaining elements of left
    # subarray into temporary array
    while i <= mid:
        temp_arr[k] = arr[i]
        k += 1
        i += 1

    # Copy the remaining elements of right
    # subarray into temporary array
    while j <= right:
        temp_arr[k] = arr[j]
        k += 1
        j += 1

    # Copy the sorted subarray into Original array
    for loop_var in range(left, right + 1):
        arr[loop_var] = temp_arr[loop_var]

    return inv_count

# Driver Code
# Given array is
arr = [1, 20, 6, 4, 5]
n = len(arr)
result = mergeSort(arr, n)
print("Number of inversions are", result)


