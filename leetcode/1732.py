class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        count = 0
        maxi = [0]
        l = len(gain)
        for i in range(l):
            count += gain[i]
            maxi.append(count)
        return max(maxi)    
