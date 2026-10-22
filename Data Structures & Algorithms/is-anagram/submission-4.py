class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        len_s = len(s)
        len_t = len(t)

        if len_s != len_t:
            return False

        hash_set = {}
        for i in range(len_s):
            hash_set[s[i]] = hash_set.get(s[i], 0) + 1
            hash_set[t[i]] = hash_set.get(t[i], 0) - 1

        flag = True
        for i in hash_set:
            if hash_set[i] != 0:
                flag = False

        return flag