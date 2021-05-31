def nextPermutation(nums):
    l = len(nums)
    if l==1:
        return nums
    i = 1
    lastIndex = -1

    while(i<l):
        if nums[i] > nums[i-1]:
            lastIndex = i
        i+=1           
    
    if lastIndex == -1:
        nums.sort()
        return nums

    index = lastIndex
    for j in range(lastIndex,l):
        if nums[j] > nums[j-1] and nums[j] < nums[index]:
            index = j
        nums[lastIndex-1], nums[index] = nums[index], nums[lastIndex-1]
        nums[lastIndex:].sort()   
    return nums

if __name__ == '__main__':
    nums = list(map(int,input().split()))
    result = nextPermutation(nums)
    print(result)


#fails on [1,3,2]   expected [1,2,3] 
