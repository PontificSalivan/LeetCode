class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        def find_max_palindrome_for_point(left_side, right_side):
            while left_side >= 0 and right_side < n and s[left_side] == s[right_side]:
                left_side -= 1
                right_side += 1

            return s[left_side+1: right_side]

        max_pol = s[0]
        for i in range(n):
            even_pol = find_max_palindrome_for_point(i, i+1)
            odd_pol = find_max_palindrome_for_point(i, i)
            max_pol = max([even_pol, odd_pol, max_pol], key=len)

        return max_pol


# test
slt = Solution()
print(slt.longestPalindrome("bababaaaasfsfsgfofofofoffoab"))
print(slt.longestPalindrome("babad"))
print(slt.longestPalindrome("cbbd"))
assert slt.longestPalindrome("babad") in ["bab", "aba"]
assert slt.longestPalindrome("cbbd") in ["bb"]
assert slt.longestPalindrome("bababaaaasfsfsgfofofofoffoab") in ["fofofofof"]
assert slt.longestPalindrome("b") in ["b"]
assert slt.longestPalindrome("ba") in ["b", "a"]
assert slt.longestPalindrome("aaffbbff55ffbbffaa") in ["aaffbbff55ffbbffaa"]
assert slt.longestPalindrome("aaffbbff55ffbbffab") in ["affbbff55ffbbffa"]
assert slt.longestPalindrome("55555555555555555") in ["55555555555555555"]
assert slt.longestPalindrome("55585") in ["555", "585"]
