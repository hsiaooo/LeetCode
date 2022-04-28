#
# @lc app=leetcode id=1370 lang=python3
#
# [1370] Increasing Decreasing String
#

# @lc code=start
class Solution:
    def sortString(self, s: str) -> str:
        res = list()
        while s:
            minCharactice = min(s)
            maxCharactice = max(s)
            print(minCharactice)
            res.append(minCharactice)
            s = s.replace(minCharactice, '')
            print(res)
# @lc code=end

