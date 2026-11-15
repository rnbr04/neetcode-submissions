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

        
        result = []
        for value in hash_map.values():
            result.append(value)

        return result