class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        strn = str(n)
        n = 1
        s = 0
        for digit in strn:
            n = n*int(digit)
            s = s+int(digit)
        return (n-s)