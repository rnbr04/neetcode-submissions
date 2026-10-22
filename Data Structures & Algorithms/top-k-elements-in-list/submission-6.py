class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        bucket = [[] for _ in range(len(nums) + 1)]

        # iterate through the array and update their frequency
        for num in nums:
            hash_map[num] = hash_map.get(num, 0) + 1

        # put the numbers in bucket according to their frequency
        for num, freq in hash_map.items():
            bucket[freq].append(num)
        
        
        # iterate through the bucket till len(result) = k
        result = []
        for i in range(len(bucket)-1, -1, -1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result