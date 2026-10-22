import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        for num in nums:
            hash_map[num] = hash_map.get(num, 0) + 1
        
        min_heap = []
        for num, cnt in hash_map.items():
            heapq.heappush(min_heap, [cnt, num])

            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        result = []
        print(min_heap)
        for pair in min_heap:
            result.append(pair[1])

        return result