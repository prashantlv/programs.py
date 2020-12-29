import numpy as np
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = len(nums)
        li = np.zeros(l,int)
        f = 0
        for i in range(l):
            if nums[i] == 1:
                li[f] += 1
            else:
                f +=1
        return max(li)        
                