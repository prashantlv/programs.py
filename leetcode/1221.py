class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        flag = 0
        for letter in s:
            if letter == 'R':
                count += 1
            else:
                count -= 1
            if count == 0:
                flag += 1
        return flag