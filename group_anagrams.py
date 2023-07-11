from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            sorted_s = "".join(sorted(list(s)))
            anagrams[sorted_s] = anagrams.get(sorted_s, []) + [s]
        return list(anagrams.values())


# test
slt = Solution()
print(slt.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
# assert slt.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) ==

