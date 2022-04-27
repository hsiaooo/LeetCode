#
# @lc app=leetcode id=263 lang=python3
#
# [263] Ugly Number
#

# @lc code=start
import re

class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 1:
            return True

        elif n <= 0:
            return False

        else:
            while n % 2 == 0:
                n /= 2
            while n % 3 == 0:
                n /= 3
            while n % 5 == 0:
                n /= 5
            
            if n == 1:
                return True

            else:
                return False

# @lc code=end

