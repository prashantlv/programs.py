#Naive solution

def maxProfit(self, prices: List[int]) -> int:
    l = len(prices)
    max = 0
    for i in range(l):
        for j in range(i+1,l):
            temp = prices[j]-prices[i]
            if temp > max:
                max = temp
    return max

#########ONE PASS#############

def maxProfit(self, prices: List[int]) -> int:
    l = len(prices)
    minimum = 2222222222
    maximum = 0
    for i in range(l):
        if (prices[i] < minimum):
            minimum = prices[i]
        elif (prices[i]-minimum > maximum):
            maximum = prices[i] - minimum
    return maximum        
