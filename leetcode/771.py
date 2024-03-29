class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        J = set(J)
        count = 0
        for letter in S:
            if letter in J:
                count += 1
        return count

# Another one 
# return sum([S.count(j) for j in set(J)])        