class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        l = len(nums)
        count = 0
        for i in range(l):
            for j in range(i):
                if nums[i] == nums[j]:
                    count += 1
                else:
                    pass
        return count