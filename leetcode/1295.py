class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        li = []
        for i in nums:
            while(i>0):
                i = i//10
                count += 1
            if count % 2 == 0:
                li.append(1)
            else:
                pass
            count = 0
        return len(li)    