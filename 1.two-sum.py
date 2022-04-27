#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create a dict to store the num and index
        buffer = {}
        # search number one by one
        for i, n in enumerate(nums):
            # n + m = target -> m = targer -n
            m = target - n
            # make sure not store the same number
            if m in buffer:
                # find m
                return [buffer[m], i]
            else:
                # store the first number
                buffer[n] = i
# @lc code=end

