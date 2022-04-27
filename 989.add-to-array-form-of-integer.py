#
# @lc app=leetcode id=989 lang=python3
#
# [989] Add to Array-Form of Integer
#

# @lc code=start
from itertools import count


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num = int(''.join([str(i) for i in num]))
        addNum = num + k
        res = list(map(int, str(addNum)))
        return res
# @lc code=end

