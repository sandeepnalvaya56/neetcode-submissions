import heapq
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        if n <= 1:
            return n
        # Using a set to remove duplicates makes the logic cleaner and more efficient
        sortedNums = sorted(nums)
        print("sortedNums: ", sortedNums)
        
        
        counter = 1
        longestSequence = 1
        for i in range(n-1):
            print("Counter: ", counter)
            print("longestSequence: ", longestSequence)
            print("Current Element: ", sortedNums[i])
            diffNext = sortedNums[i+1] - sortedNums[i]

            if diffNext == 1:
                counter = counter + 1
                if counter > longestSequence:
                    longestSequence = counter
            elif diffNext == 0:
                continue
            else:
                counter = 1
        return longestSequence


            

