class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_set = set()
        for i in nums:
            if i not in hash_set:
                hash_set.add(i)
            
            else:
                return True
        return False