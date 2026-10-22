class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}

        for num in nums:
            hash_map[num] = hash_map.get(num, 0) + 1

        cnt = []
        for num, count in hash_map.items():
            cnt.append([count, num])

        cnt.sort()

        output = []
        for i in range(-1, -k-1, -1):
            output.append(cnt[i][1])

        return output 
        