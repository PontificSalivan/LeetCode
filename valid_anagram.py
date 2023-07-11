class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        unique_s = set(s)
        for char_s in unique_s:
            if s.count(char_s) != t.count(char_s):
                return False
        return True


# test
slt = Solution()
print(slt.isAnagram("asas", "asas"))
print(slt.isAnagram("asas", "asa"))
print(slt.isAnagram("asassssssssssssss", "sassssssssssssssa"))
print(slt.isAnagram("asassssssssssssss", "sssssssssssssssss"))
assert slt.isAnagram("asas", "asas")
assert not slt.isAnagram("asas", "asa")
