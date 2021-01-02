class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = []
        for i in range(n):
            nums.append(start + 2*i)
        result = reduce(lambda x,y: x^y, nums)   #reduce take fun and list. Performs operation on list.
        return result