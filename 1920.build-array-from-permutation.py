#
# @lc app=leetcode id=1920 lang=python3
#
# [1920] Build Array from Permutation
#

# @lc code=start
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = list()
        for i, num in enumerate(nums):
            ans.append(nums[nums[i]])
        return ans
        
    def optimialArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            nums[i] = nums[i] + n * (nums[nums[i]] % n)
        for j in range(n):
            nums[j] = int(nums[j] / n)
        return nums
# @lc code=end

