class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        li = [x*x for x in A]
        li.sort()
        return li