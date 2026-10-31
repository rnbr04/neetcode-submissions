class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)
        res = 0
        for num in nums:
            # if beginning of a sequence
            if (num - 1) not in hash_set:
                curr, streak = num, 0
                while curr in hash_set:
                    curr += 1
                    streak += 1
                res = max(res, streak)

        return res