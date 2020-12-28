class Solution:
    def generateTheString(self, n: int) -> str:
        stri = ''
        ast = 'p'
        bst = 'z'
        if n%2 != 0:
            stri = n*ast
        else:
            stri = (n-1)*ast + bst
        return stri