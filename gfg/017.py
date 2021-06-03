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
#Graph concept
#find the largest peak following the smallest valley. We can maintain two variables - minprice and maxprofit corresponding to the smallest valley and maximum profit (maximum difference between selling price and minprice) obtained so far respectively.

def maxProfit(self, prices: List[int]) -> int: 
    l = len(prices)
    minprice = max(prices) +1
    maxprofit = 0 
    for i in range(l):
        if (prices[i] < minprice):
            minprice = prices[i]
        elif (prices[i]-minprice > maxprofit):
            maxprofit = prices[i] - minprice
    return maxprofit
