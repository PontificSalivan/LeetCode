
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        nums = nums1 + nums2
        nums_len = len(nums)
        nums.sort()
        if nums_len % 2:
            median = nums[int((nums_len - 1) / 2)]
        else:
            median = (nums[int(nums_len / 2) - 1] + nums[int(nums_len / 2)]) / 2
        return median


# test
s = Solution()
print(s.findMedianSortedArrays(nums1=[1, 3], nums2=[2]))
print(s.findMedianSortedArrays(nums1=[1, 2, 96], nums2=[3, 4, 78]))
