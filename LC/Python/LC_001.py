""" 001 - Two Sum
https://leetcode.com/problems/two-sum/

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution.
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        past_nums = {}
        for i, n in enumerate(nums):
            if target-n in past_nums:
                return [past_nums[target-n], i]
            else:
                past_nums[n] = i

if __name__ == "__main__":
    solution = Solution()
    nums = [2, 7, 11, 15]
    target = 9

    print "Given nums = {}, target = {}".format(nums, target)
    print "Expected output: [0, 1]"
    print "Output = {}".format(solution.twoSum(nums, target))
