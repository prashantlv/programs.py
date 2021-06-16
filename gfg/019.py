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
