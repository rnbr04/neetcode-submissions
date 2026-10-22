from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        ord_a = ord("a")
        #O(N) = length of list
        for word in strs:
            count = [0] * 26
            #O(M), M = length of word
            for char in word:
                count[ord(char) - ord_a] += 1

            result[tuple(count)].append(word)

        return list(result.values())

        #Net time complexity: O(N*M)
        #Net space complexity: O(26+M*N) = O(N*M)
