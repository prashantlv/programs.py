class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxi = 0
        for i in range(len(accounts)):
            maxi = max(maxi,sum(accounts[i]))
        return maxiY8TMDCD2CE