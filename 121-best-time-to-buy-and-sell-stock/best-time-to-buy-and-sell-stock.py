class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        minbuy=prices[0]
        for i in range(1,len(prices)):
            profit=max(profit,prices[i]-minbuy)
            minbuy=min(minbuy,prices[i])
        return profit
        