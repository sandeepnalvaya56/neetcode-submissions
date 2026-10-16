from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        freqMap = Counter(nums)
        # # Heapq Implementation
        # heap = []
        # # So we have number, occurence as key,value
        # # We need a sorted list based on occurence
        # # Lets implement heapq - minheap etc
        # for key, value in freqMap.items():
        #     heapq.heappush(heap, (value,key))
        #     if len(heap) > k:
        #         heapq.heappop(heap)
        # return [i[1] for i in heap]

        ## BubbleSort Implementation
        # We create a list with frequencies of elements, index representing the frequencies and empty lists carrying the numbers which have those frequencies
        n = len(nums)
        temp = [[] for _ in range(n+1)]
        for key, value in freqMap.items():
            temp[value].append(key)
        for i in range(n, -1, -1):
            for num in temp[i]:
                result.append(num)
                if len(result) == k:
                    return result




        


