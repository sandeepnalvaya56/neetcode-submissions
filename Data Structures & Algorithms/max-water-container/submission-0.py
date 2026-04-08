class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxAmount = 0
        n = len(heights)

        for i in range(n-1):
            for j in range(i+1, n):
                amount = min(heights[i],heights[j]) * (j-i)
                maxAmount = max(amount, maxAmount)
        return maxAmount
