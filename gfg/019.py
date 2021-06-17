# Approach 01
def commonElements (self,A, B, C, n1, n2, n3):
    # your code here
    n = min(n1,n2,n3)
    arr =[]
    test_array = []
    if n == n1:
        test_array = A
    elif n == n2:
        test_array = B
    else:
        test_array = C
    for element in test_array:
        if element in A and element in B and element in C:
            if element not in arr:
                arr.append(element)
    return arr

# Approach 02 intersection b/w 2 array

def commonElements (self,A, B, C, n1, n2, n3):
    # your code here
    arr =[]
    i, j = 0, 0
    while (i<n1 and j<n2):
        if A[i] < B[j]:
            i += 1
        elif B[j] < A[i]:
            j += 1
        else:
            arr.append
    arr = [arr.remove(element) for element in arr if element not in C]
    return arr

# Approach 03 find frequency of each element in array without duplicates

def commonElements (self,A, B, C, n1, n2, n3):
    A, B, C = set(A), set(B), set(C)
    temp_array = list(A) + list(B) + list(C)
    # now find frequncy for temp_array and print elements with freq, 3
