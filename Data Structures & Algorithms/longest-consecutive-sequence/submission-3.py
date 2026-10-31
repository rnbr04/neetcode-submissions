# Brute-Force
# Create a set from the list: O(N)
# Iterate through each number: O(N)
    # Create a streak from it O(N)
# if it breaks, update res with longest streak
# T = O(N) + O(N^2)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        store = set(nums)

        for num in nums:
            streak, curr = 0, num
            while curr in store:
                streak += 1
                curr += 1
            
            res = max(res, streak)
        return res
