from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ord_a = ord('a')
        hash_map = defaultdict(list) 
        for word in strs:
            bucket = [0] * 26
            for letter in word:
                bucket[ord(letter)-ord_a] += 1

            hash_map[tuple(bucket)].append(word)
        
        return list(hash_map.values())
