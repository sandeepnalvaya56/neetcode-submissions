class Solution:
    # def maxProfit(self, prices: List[int]) -> int:
    #     n = len(prices)
    #     maxProfit = 0
    #     for i in range(len(prices)):
    #         for j in range(i+1, len(prices)):
    #             currProfit = prices[j] - prices [i]
    #             maxProfit = max(currProfit, maxProfit)
    #     return maxProfit

    # def maxProfit(self, prices: List[int]) -> int:
    #     n = len(prices)
    #     maxProfit = 0
    #     l = 0
    #     r = 1
    #     while r < n:
    #         if prices[l] < prices[r]:
    #             currProfit = prices[r] - prices[l]
    #             maxProfit = max(currProfit, maxProfit)
    #         else:
    #             l = r
    #         r = r+1
    #     return maxProfit
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = float('inf')
        maxProfit = 0
        currProfit = 0
        i = 0
        while i < (len(prices) -1):
            minPrice = min(minPrice, prices[i])
            currProfit = prices[i+1] - minPrice
            maxProfit = max(maxProfit, currProfit)
            i += 1
        return maxProfit


