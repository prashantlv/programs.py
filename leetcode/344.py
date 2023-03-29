class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        # """
        ## string operator

        # reverse = ""
        # temp = ""
        # for ch in s:
        #     temp = reverse
        #     reverse = ch + temp

        ## One liner
        s[:] = s[::-1]

        ## swap first and last
        # r = len(s)-1
        # l = 0

        # while(l<r):
        #   temp = s[r]
        #   s[r] = s[l]
        #   s[l] = temp
        #   l+=1
        #   r-=1
