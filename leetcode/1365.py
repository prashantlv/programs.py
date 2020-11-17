class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        a = []
        count = 0
        leng = len(nums)
        for i in range(leng):
            for j in range(leng):
                if nums[i] > nums[j]:
                    count += 1
            a.append(count)
            count = 0
        return a    
            