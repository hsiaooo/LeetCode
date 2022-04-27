#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start

class Solution:
    def isValid(self, s: str) -> bool:
        d = {')':'(', ']':'[', '}':'{'}
        pars = [None]
        for c in s:
            if c in d:
                if d[c] != pars.pop():
                    return False
            else:
                pars.append(c)

        return len(pars) == 1


# @lc code=end