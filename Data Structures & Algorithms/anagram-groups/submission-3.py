class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        for string in strs:
            hash_bucket = [0] * 26
            for letter in string:
                hash_bucket[ord(letter) - ord('a')] += 1

            if tuple(hash_bucket) not in hash_map:
                hash_map[tuple(hash_bucket)] = [string]
            else:
                hash_map[tuple(hash_bucket)].append(string)

        
        return list(hash_map.values())