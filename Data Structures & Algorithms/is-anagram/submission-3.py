from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_hash = defaultdict(int)
        for char in s:
            s_hash[char] += 1
        
        for char in t:
            s_hash[char] -= 1

        flag = True
        for char in s_hash:
            if s_hash[char] != 0:
                flag = False

        return flag