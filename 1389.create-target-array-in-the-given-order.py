#
# @lc app=leetcode id=1389 lang=python3
#
# [1389] Create Target Array in the Given Order
#

# @lc code=start
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        res = list()

        for num, idx in zip(nums, index):
            if len(res) > idx:
                res.insert(idx, num)

            else:
                res.append(num)            

        return res
# @lc code=end

