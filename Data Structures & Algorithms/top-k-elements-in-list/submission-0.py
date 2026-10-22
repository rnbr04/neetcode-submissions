class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}

        for num in nums:
            hash_map[num] = 1 + hash_map.get(num, 0)

        count = []
        for num, cnt in hash_map.items():
            count.append([cnt, num])
        
        count.sort()

        result = []
        while len(result) < k:
            result.append(count.pop()[1])
    
        return result 