class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        for i in range(len(prices)):
            k = i+1
            while k<len(prices) and prices[k]>prices[i]:
                k += 1
            if k < len(prices):
                prices[i] -= prices[k]
        return prices

