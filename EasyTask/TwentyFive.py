from typing import List
#1. https://leetcode.com/problems/split-the-array/description/
def isPossibleToSplit(self, nums: List[int]) -> bool:
    nums.sort()
    res1 = []
    res2 = []
    for i in range(0, len(nums) - 1, 2):
        res1.append(nums[i])
        res2.append(nums[i + 1])
    return len(res1) == len(set(res1)) and len(res2) == len(set(res2))

#2. https://leetcode.com/problems/delete-characters-to-make-fancy-string/description/
def makeFancyString(self, s: str) -> str:
    arr = list(set(s))
    for i in arr:
        if s.count(i) >= 3:
            while True:
                lenS = len(s)
                s = s.replace(i * 3, i * 2)
                if len(s) == lenS: break
    return s

#3. https://leetcode.com/problems/lemonade-change/description/
def lemonadeChange(self, bills: List[int]) -> bool:
    change = []
    for i in bills:
        if i == 5: change.append(5)
        elif i == 10:
            try:
                change.remove(5)
                change.append(10)
            except ValueError: return False
        else:
            try:
                if change.count(10) >= 1:
                    change.remove(5)
                    change.remove(10)
                else:
                    change.remove(5)
                    change.remove(5)
                    change.remove(5)
            except ValueError: return False
    return True
#4.
#5.
#6.
#7.
#8.
#9.
#10.