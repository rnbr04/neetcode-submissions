class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set()
        res = 0
        if len(nums) == 1:
            return 1
            
        for i in nums:
            if (i - 1) in nums:
                res += 1
            hash_set.add(i)

        return res