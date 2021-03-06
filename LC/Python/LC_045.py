""" 045 - Jump Game II
https://leetcode.com/problems/jump-game-ii/

Given an array of non-negative integers, you are initially positioned at the
first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. (Jump 1 step from
index 0 to 1, then 3 steps to the last index.)
"""


class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        left = 0
        count = 0
        if length == 1:
            return 0
        while left < length:
            count += 1
            j = nums[left]
            if left + j >= length-1:
                break
            next_jump = [i+v for i, v in enumerate(nums[left+1:left+1+j])]
            left += next_jump.index(max(next_jump)) + 1

        return count
