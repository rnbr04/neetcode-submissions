# Min-Heap
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        for num in nums:
            hash_map[num] = 1 + hash_map.get(num, 0)

        min_heap = []
        for num, cnt in hash_map.items():
            heapq.heappush(min_heap, (cnt, num))

            if len(min_heap) > k:
                heapq.heappop(min_heap)

        result = []
        for i in range(k):
            result.append(heapq.heappop(min_heap)[1])

        return result

        