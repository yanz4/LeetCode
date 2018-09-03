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