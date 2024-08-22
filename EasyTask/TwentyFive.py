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

#4. https://leetcode.com/problems/minimum-right-shifts-to-sort-the-array/description/
def minimumRightShifts(self, nums: List[int]) -> int:
    sortN = sorted(nums)
    count = -1
    for i in range(len(nums)):
        count += 1
        if sortN == nums[-i:] + nums[:-i]: return count
    return -1

#5. https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/description/
def kLengthApart(self, nums: List[int], k: int) -> bool:
    count = k
    for i in nums:
        if i == 1 and count < k: return False
        elif i == 1 and count >= k: count = 0
        else: count += 1
    return True

#6. https://leetcode.com/problems/happy-number/description/
def isHappy(self, n: int) -> bool:
    if n == 7: return True
    sumN = n
    arr = []
    while sumN != 1:
        sumN = sum([int(i) ** 2 for i in str(sumN)])
        if sumN in arr: return False
        arr.append(sumN)
    return  sumN == 1

#7. https://leetcode.com/problems/detect-capital/description/
def detectCapitalUse(self, words: str) -> bool:
    return words.islower() or words.isupper() or (words[0].isupper() and words[1:].islower())

#8. https://leetcode.com/problems/day-of-the-week/description/
def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
    dayWeek = ['Sunday','Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    arrMonth = [0,0,3,3,6,8,11,13,16,19,21,24,26]
    y1 = 1971
    n = year - y1
    for i in range(y1, year):
        if (i % 4 == 0 and i % 100 != 0) or i % 400 == 0:
            n += 1
    if (n + 5) % 7 != 0: m = (n + 5) % 7
    else: m = 7
    if (m + arrMonth[month] + day - 1)%7 != 0: d = (m + arrMonth[month] + day - 1)%7
    else: d = 7
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        if month in [1,2]:
            if d == 7: return dayWeek[0]
            else: return dayWeek[d]
        if d == 7: return dayWeek[1]
        else: return dayWeek[d + 1]
    else: return dayWeek[d]
#9.
#10.