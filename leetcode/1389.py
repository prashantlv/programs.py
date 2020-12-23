class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        ln = len(nums)
        new_arr = []
        for i in range(ln):
            new_arr.insert(index[i],nums[i])
        return new_arr