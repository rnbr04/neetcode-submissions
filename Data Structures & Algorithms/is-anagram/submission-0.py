from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash = defaultdict(int)
        for char in s:
            s_hash[char] += 1
        
        for char in t:
            if char in s_hash:
                s_hash[char] -= 1

        for char in s_hash:
            if s_hash[char] == 0:
                continue
            else:
                return False

        return True