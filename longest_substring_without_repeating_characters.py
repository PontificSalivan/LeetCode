class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub_s = ''
        max_subs = 0
        for i in s:
            if i not in sub_s:
                sub_s += i
            else:
                len_subs = len(sub_s)
                max_subs = len_subs if len_subs > max_subs else max_subs
                sub_s = sub_s[sub_s.index(i)+1:] + i

        max_subs = len(sub_s) if len(sub_s) > max_subs else max_subs
        return max_subs


# test
slt = Solution()
print(slt.lengthOfLongestSubstring("abcabcbb"))
print(slt.lengthOfLongestSubstring("bbbbb"))
print(slt.lengthOfLongestSubstring("pwwkew"))
print(slt.lengthOfLongestSubstring(" "))
print(slt.lengthOfLongestSubstring("aab"))
print(slt.lengthOfLongestSubstring("dvdf"))
assert slt.lengthOfLongestSubstring("abcabcbb") == 3
assert slt.lengthOfLongestSubstring("bbbbb") == 1
assert slt.lengthOfLongestSubstring("pwwkew") == 3
assert slt.lengthOfLongestSubstring("qwertyyyyyyyyyyyy") == 6
assert slt.lengthOfLongestSubstring(" ") == 1
assert slt.lengthOfLongestSubstring("aab") == 2
assert slt.lengthOfLongestSubstring("dvdf") == 3
assert slt.lengthOfLongestSubstring("") == 0
