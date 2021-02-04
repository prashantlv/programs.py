class Solution:
    ef kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        a =[]
        m = max(candies)
        for i in candies:
            if i+extraCandies < m:
                a.append(False)
            else:
                a.append(True)
        return a
            
