class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Remember the constraints: O(n) time and no division operator.
        nums_length = len(nums)

        #count zeroes
        z=0
        zero_index = -1
        
        i=0
        while i < nums_length :
            if nums[i] == 0:
               z+=1
               zero_index = i
            i+=1
        
        if z>1:
            return [0 for _ in nums]
            	
        
        
        multiple = 1
        
        for num in nums:
            if num != 0:
                multiple *= num
        print(multiple)
        
        result=[]
        i=0
        while i < nums_length :
            if z == 1 and i != zero_index:
                result.append(0)
            elif z == 1 and i == zero_index:
                result.append(multiple)
            else:
                result.append(int(multiple/nums[i]))
            i+=1
        
        return result
