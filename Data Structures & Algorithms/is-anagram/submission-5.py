# this is double iteration

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hash_s = {}
        hash_t = {}

        for letter in s:
            hash_s[letter] = hash_s.get(letter, 0) + 1

        for letter in t:
            hash_t[letter] = hash_t.get(letter, 0) + 1

        for i in hash_s:
            if i not in hash_t:
                return False
            elif hash_s[i] == hash_t[i]:
                continue
            elif hash_s[i] != hash_t[i]:
                return False

        return True
