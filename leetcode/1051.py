class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sortd = sorted(heights)
        count = 0
        for i,j in zip(sortd, heights):
            if i!=j:
                count += 1
        return count        
# zip(list1, list2) = [(a1,a2),(b1,b2),(c1.c2)]    
    