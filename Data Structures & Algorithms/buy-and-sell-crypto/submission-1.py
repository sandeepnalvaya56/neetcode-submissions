class Solution:
    # def maxProfit(self, prices: List[int]) -> int:
    #     n = len(prices)
    #     maxProfit = 0
    #     for i in range(len(prices)):
    #         for j in range(i+1, len(prices)):
    #             currProfit = prices[j] - prices [i]
    #             maxProfit = max(currProfit, maxProfit)
    #     return maxProfit

    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        maxProfit = 0
        l = 0
        r = 1
        while r < n:
            if prices[l] < prices[r]:
                currProfit = prices[r] - prices[l]
                maxProfit = max(currProfit, maxProfit)
            else:
                l = r
            r = r+1
        return maxProfit


