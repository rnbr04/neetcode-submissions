class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for i, num_1 in enumerate(nums):
            num_2 = target - num_1
            
            if num_2 in hash_map:
                j = hash_map[num_2]
                if i < j:
                    return [i, j]
                else:
                    return [j, i]

            else:
                hash_map[num_1] = i