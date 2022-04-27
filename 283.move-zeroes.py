#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i, num in enumerate(nums):
            if num == 0:
                nums.append(num)
                print('Before pop: ', nums)
                nums.pop(i)
                print('After pop: ', nums)
            else: pass
# @lc code=end

