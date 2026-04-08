
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Funda 1: There is one messy half and one one sorted half
        # Funda 2: Always compare mid to right
        # Funda 3: If your answer lies 100% within the array, then use left < right to trap the answer, meaning leave precisely one element before exiting the loop
        # Funda 4: If your answer lies maybe or may not be in array, then use left <= right condition and let left increment more than right to exit
        # When moving the pointers, if you are on unsorted end (mid>right), always move the left pointer to mid + 1 because anything on the left is sorted and has to be bigger than right, including the mid itself which we just tested
        # If you are on sorted end (mid<right), move the right pointer to mid, because mid can be the starting point or inflection point or part of fully sorted array


        left = 0
        right = len(nums) -1
        result = float('inf')
        # Here we need trap strategy
        # [3,4,5,6,1,2]
        # [1,2,3,4,5,6]
        counter = 0
        while left < right:
            print("left:", left)
            print("right:", right)
            mid = left + (right-left)//2
            print("mid:", mid)
            counter +=1
            if nums[mid] > nums[right]:
                left = mid+1
                print("Went inside mid > right mid:", nums[mid])
            else:
                right = mid
                print("Went inside else right = mid")
            print(nums[left], nums[mid], nums[right] )
            if counter > 10:
                print("counter:", counter)
                break
        return nums[left]

            

