class Solution:
    def findMin(self, nums: List[int]) -> int:
        #nums = [3,4,5,6,1,2]
        #[4,5,6,7,0,1,2,3]
        left = 0
        right = len(nums) - 1
        result = nums[0]
        while left < right:
            mid = left + (right - left)//2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid+1
        return nums[left]

        

        