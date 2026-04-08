from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        We need to count the frequence of each element and store it in the hashmap
        Then we create a list with k elements
        We will iterate through the dictionary (outer iteration)
        we will iterate through the k elements list
        We will check if the first element is smaller than the dictionary value, if yes, then we will add it to the first index,
         then we will pop the last element from the list, 
        for each element we will traverse through the k element list untill we find a number smaller than current number
        then we will return the k element list
        """

        """ Initial Solution By Me:
        seen = {}
        
        # create hashmap of counts
        for num in nums:
            if num in seen:
                seen[num]  += 1
            else:
                seen[num] = 1
        
        # Initialize k frequent elements list and their counts list
        elements = [0]*k
        counts = [0]*k
        for key in seen.keys(): # Iterating through the dictionary
            for i in range(len(counts)):
                if counts[i] <= seen[key]:
                    counts.insert(i, seen[key])
                    elements.insert(i, key)
                    counts.pop()
                    elements.pop()
                    break
        return elements  
        """
        freqMap = Counter(nums)
        heap = []
        for key, value in freqMap.items():
            heapq.heappush(heap, (value, key))
            if len(heap) > k:
                heapq.heappop(heap)
        return [i[1] for i in heap]
