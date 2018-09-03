'''Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:
Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''


class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]

        """

        a = []
        nums.sort()
        for i in range(len(nums) - 2):
            x = nums[i]
            if x != nums[i - 1] or i == 0:

                l = i + 1
                r = len(nums) - 1
                while l < r:
                    y = nums[l]
                    if y != nums[l - 1] or l == i + 1:
                        z = nums[r]
                        s = x + y + z
                        if s == 0:
                            a.append([x, y, z])
                            l += 1
                            r -= 1
                        elif s > 0:
                            r -= 1
                        else:
                            l += 1
                    else:
                        l += 1

        return a
