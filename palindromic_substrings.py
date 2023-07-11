class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        def find_palindrome_count_for_point(left_side, right_side):
            count = 0
            while left_side >= 0 and right_side < n and s[left_side] == s[right_side]:
                left_side -= 1
                right_side += 1
                count += 1
            return count

        palindrome_count = 0
        for i in range(n):
            even_pol_count = find_palindrome_count_for_point(i, i + 1)
            odd_pol_count = find_palindrome_count_for_point(i, i)
            palindrome_count += odd_pol_count + even_pol_count

        return palindrome_count


# test
slt = Solution()
print(slt.countSubstrings("aaaaa"))
print(slt.countSubstrings("aaaaab"))
print(slt.countSubstrings("aaaaabaaaaa"))
print(slt.countSubstrings("abaabaaba"))
print(slt.countSubstrings("aaaa"))
print(slt.countSubstrings("aaa"))
print(slt.countSubstrings("abc"))
assert slt.countSubstrings("aaaaa") == 15
assert slt.countSubstrings("aaaaab") == 16
assert slt.countSubstrings("aaaaabaaaaa") == 36
assert slt.countSubstrings("abaabaaba") == 21
assert slt.countSubstrings("aaaa") == 10
assert slt.countSubstrings("aaa") == 6
assert slt.countSubstrings("abc") == 3
