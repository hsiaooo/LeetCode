#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # count = 0
        # for i, num in enumerate(nums):
        #     if num in nums[i+1:] :
        #         pass
        #     else:
        #         count += 1
        # return count
        res = list(set(nums))
        print(res)
        return len(res)
# @lc code=end

