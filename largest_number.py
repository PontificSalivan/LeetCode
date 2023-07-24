from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        max_len = len(str(max(nums)))
        nums = [str(num) for num in nums]

        # 3 > 30 because 333 > 3030 because 333 > 303
        nums.sort(key=lambda x: x * (max_len // len(x) + 1), reverse=True)
        largest_number = '0' if nums[0] == '0' else ''.join(nums)
        return largest_number


slt = Solution()
print(slt.largestNumber([10, 2]))
print(slt.largestNumber([3,30,34,5,9]))
print(slt.largestNumber([199, 9, 95, 9999, 9567, 90, 90010]))
assert slt.largestNumber([10, 2]) == "210"
assert slt.largestNumber([3,30,34,5,9]) == "9534330"
