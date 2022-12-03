from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums_len = len(nums)
        pure_list = [0] * nums_len
        for number in nums:
            if nums_len >= number > 0:
                pure_list[number-1] = number

        for index in range(nums_len):
            if not pure_list[index]:
                return index + 1

        return nums_len + 1


# test
slt = Solution()
print(slt.firstMissingPositive([-200, -1, 3, 2, 1, -5, -3]))
print(slt.firstMissingPositive([1, 2, 3]))
print(slt.firstMissingPositive([5, 9, 8]))
print(slt.firstMissingPositive([86, 50, 5, 2, 0, 1, 3, 4, 7, 22]))
print(slt.firstMissingPositive([1, 2, 0]))
print(slt.firstMissingPositive([3, 4, -1, 1]))
print(slt.firstMissingPositive([7, 8, 9, 11, 12]))
assert slt.firstMissingPositive([1, 2, 0]) == 3
assert slt.firstMissingPositive([3, 4, -1, 1]) == 2
assert slt.firstMissingPositive([7, 8, 9, 11, 12]) == 1
assert slt.firstMissingPositive([86, 50, 5, 2, 0, 1, 3, 4, 7, 22]) == 6
assert slt.firstMissingPositive([5, 9, 8]) == 1
assert slt.firstMissingPositive([-200, -1, 3, 2, 1, -5, -3]) == 4
