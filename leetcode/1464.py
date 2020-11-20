class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxx1 = max(nums)
        nums.remove(maxx1)
        maxx2 = max(nums)
        temp=(maxx1-1)*(maxx2-1)
        return temp