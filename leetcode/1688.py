class Solution:
    def numberOfMatches(self, n: int) -> int:
        m = 0
        while n > 1 :
            if n % 2 == 0:
                n = n//2
                m += n
            else :
                n = (n+1) // 2
                m += n-1
        return m