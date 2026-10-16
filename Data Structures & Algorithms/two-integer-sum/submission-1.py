class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        n = len(nums) #4
        for i in range(n): #0,1,2,3
            lookup = target - nums[i] #7-3=4
            if lookup in seen:
                return [seen[lookup], i]
            else:
                seen[nums[i]] = i

