#1. https://leetcode.com/problems/score-of-a-string/description/
def scoreOfString(self, s: str) -> int:
    res = 0
    for i in range(len(s) - 1):
        res += abs(ord(s[i]) - ord(s[i + 1]))
    return res
#2. https://leetcode.com/problems/find-the-maximum-achievable-number/
def theMaximumAchievableX(self, num: int, t: int) -> int:
    return num + t + t