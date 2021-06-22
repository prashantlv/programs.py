def maxProduct(self,arr, n):
    # code here
    prod, temp = 1, arr[0]
    for i in range(n):
        if arr[i] == 0: # if 0 arrives in middel
            prod = 1
        else:
            prod = prod*arr[i]
        if prod > temp:
            temp = prod
    return temp

# failing in test case with first negative and rest positive elements // need to skip those numbers from front    
