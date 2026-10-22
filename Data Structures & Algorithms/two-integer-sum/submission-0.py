class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i, nums1 in enumerate(nums):
            nums2 = target - nums1

            if nums2 in hash_map:
                r1 = min(i, hash_map[nums2])
                r2 = max(i, hash_map[nums2])
                return [r1, r2]

            hash_map[nums1] = i
