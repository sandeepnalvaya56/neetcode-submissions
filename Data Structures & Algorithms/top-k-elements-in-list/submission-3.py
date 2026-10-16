from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        freqMap = Counter(nums)
        heap = []
        # So we have number, occurence as key,value
        # We need a sorted list based on occurence
        # Lets implement heapq - minheap etc
        for key, value in freqMap.items():
            heapq.heappush(heap, (value,key))
            if len(heap) > k:
                heapq.heappop(heap)
        return [i[1] for i in heap]


