class Solution:
    def sumZero(self, n: int) -> List[int]:
        li = []
        if n % 2 == 1 :
            li.append(0)
        
        for i in range(1, n//2 +1):
            li.append(i)
            li.append(-i)
        return li 
