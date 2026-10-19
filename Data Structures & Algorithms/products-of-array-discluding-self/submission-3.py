class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        left_arr = []
        right_arr = []
        result = []
        
        n=len(nums)

        left_product = 1
        
        for i in range(n):
            result.append(left_product)
            left_product = left_product*nums[i]
        
        right_product = 1
        
        for i in range(n-1, -1, -1):
            result[i] = result[i]*right_product
            right_product = right_product*nums[i]
        
        return result