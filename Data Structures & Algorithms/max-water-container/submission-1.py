class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # maxAmount = 0
        # n = len(heights)

        # for i in range(n-1):
        #     for j in range(i+1, n):
        #         amount = min(heights[i],heights[j]) * (j-i)
        #         maxAmount = max(amount, maxAmount)
        # return maxAmount
        maxAmount = 0
        n = len(heights)-1
        i=0
        while i < n:
            amount = min(heights[i],heights[n]) * (n-i)
            maxAmount = max(amount, maxAmount)
            if heights[i] <= heights[n]:
                i = i+1
            else:
                n = n-1
        return maxAmount
            
        

