class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # T = O(N)
        hash_set = set(nums)
        res = 0
        # T = O(N), here the while loop does not run O(N) for each num
        # instead if it is beginning of a sequence then it iterates over other elements
        # so, on avg it runs for O(N)
        for num in nums:
            # if beginning of a sequence
            if (num - 1) not in hash_set:
                curr, streak = num, 0
                while curr in hash_set:
                    curr += 1
                    streak += 1
                res = max(res, streak)

        return res

# T = O(N + N) = O(N)
