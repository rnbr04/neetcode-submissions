class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_map = {}
        
        for i in nums:
            # if num does not exist in hash_map
            if hash_map.get(i, -1) == -1:
                hash_map[i] = 1
            # else if it exists, mark it as duplicate occurrence
            else:
                return True

        # if complete list iterated, then no duplicate found
        return False


