class Solution:
    def search(self, nums: List[int], target: int) -> int:
        temp = -1
        for i in range(len(nums)):
            if nums[i] == target:
                temp = i
            else:
                pass
        return temp