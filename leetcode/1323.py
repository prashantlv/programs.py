class Solution:
    def maximum69Number (self, num: int) -> int:
        num = [x for x in str(num)]
        l=len(num)
        for y in range(l):
            if num[y] == '6':
                num[y] = '9'
                break 
        return int(''.join(num))
