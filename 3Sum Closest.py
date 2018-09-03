'''Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).'''



class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        import numpy as np
        nums.sort()
        a = []
        s = True
        index = []

        for i in range(len(nums) - 2):
            x = nums[i]
            if x != nums[i - 1] or i == 0:
                for j in range(i + 1, len(nums) - 1):
                    y = nums[j]
                    if y != nums[j - 1] or j == i + 1:
                        l = j + 1
                        r = len(nums) - 1
                        while l <= r:
                            if l == r:
                                index.append([i, j, l])
                                break
                            else:
                                ls = x + y + nums[l] - target
                                rs = x + y + nums[r] - target
                                if ls * rs == 0:
                                    return target
                                elif ls * rs > 0:
                                    if rs > 0:
                                        index.append([i, j, l])
                                        if l != j + 1:
                                            index.append([i, j, l - 1])
                                    else:
                                        index.append([i, j, r])
                                        if r != len(nums) - 1:
                                            index.append([i, j, r + 1])
                                    break
                                else:
                                    if r - l == 1:
                                        if ls + rs > 0:
                                            index.append([i, j, l])
                                        else:
                                            index.append([i, j, r])
                                        break
                                    else:
                                        l += 1
                                        r -= 1
        b = index
        for e in b:
            a.append((nums[e[0]] + nums[e[1]] + nums[e[2]] - target) ** 2)
        ind = b[np.argmin(a)]

        return (nums[ind[0]] + nums[ind[1]] + nums[ind[2]])


aaa = Solution()
nums = [-1, 0, 1, 1, 55]
target = 3

print(aaa.threeSumClosest(nums, target))
