class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        left = 0
        right = len(nums) - 1
        while left <= right:
            # [3,4,5,6,1,2]
            # Middle Index Calculate
            if target == nums[left]:
                return left
            elif target == nums[right]:
                return right
            else:
                mid = left + (right - left)//2
                if nums[mid] == target:
                    return mid
            
            # If nothing returned anything, which part we are in?
            if nums[mid] > nums[right]: # the left half is sorted
                if target < nums[mid] and target > nums[left]: # if number is in left half, move right index to mid to discard unsorted part
                    right = mid-1
                    if nums[mid] == target:
                        return mid
                else:
                    left = mid+1 # if not, move left index to mid+1 to discard sorted part
            else: # if right half is sorted. means nums[mid] must be smaller than nums[right]
                if target > nums[mid] and target < nums[right]: # number is in sorted part
                    left = mid+1 # discard unsorted part
                    if nums[mid] == target:
                        return mid
                else:
                    right = mid - 1 # discard sorted part
        return -1

        





                


        