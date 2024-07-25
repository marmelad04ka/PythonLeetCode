from typing import List
#1. https://leetcode.com/problems/largest-odd-number-in-string/description/
def largestOddNumber(self, num: str) -> str:
    l1 = num[::-1]
    res = ''
    for i in range(len(l1)):
        if int(l1[i]) % 2 != 0:
            res += l1[i:]
            break
    return res[::-1]

#2. https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/description/
def average(self, salary: List[int]) -> float:
    salary.sort()
    return sum(salary[1:len(salary) - 1])/len(salary[1:len(salary) - 1])

#3. https://leetcode.com/problems/valid-parentheses/description/
def isValid(self, s: str) -> bool:
    if len(s)%2 != 0: return False
    res = ''
    for i in s:
        if i in '({[': res += i
        elif len(res) != 0 and ((i == ')' and res[-1] == '(') or (i == ']' and res[-1] == '[') or (i == '}' and res[-1] == '{')): res = res[:-1]
        else: return False
    return res == ''

#4. https://leetcode.com/problems/min-max-game/description/
def minMaxGame(self, nums: List[int]) -> int:
    res = []
    count = 0
    while len(nums) != 1:
        for i in range(0, len(nums) - 1, 2):
            if count%2 == 0:
                res.append(min(nums[i], nums[i + 1]))
            else: res.append(max(nums[i], nums[i + 1]))
            count += 1
        nums = res
        res = []
    return nums[0]

#5. https://leetcode.com/problems/sum-of-digits-of-string-after-convert/description/
def getLucky(self, s: str, k: int) -> int:
    s1 = ''.join([str(ord(i) - 96) for i in s])
    for i in range(1, k + 1):
        s1 = str(sum([int(i) for i in s1]))
    return int(s1)

#6. https://leetcode.com/problems/circular-sentence/description/
def isCircularSentence(self, sentence: str) -> bool:
    l1 = sentence.split(" ")
    for i in range(len(l1)):
        if i == len(l1) - 1:
            if l1[i][-1] == l1[0][0]: break
            else: return False
        if l1[i][-1] != l1[i + 1][0]: return False
    return True

#7. https://leetcode.com/problems/sort-even-and-odd-indices-independently/description/
def sortEvenOdd(self, nums: List[int]) -> List[int]:
    res = [0 if i%2 == 0 else 1 for i in range(len(nums))]
    odd = sorted([nums[i] for i in range(len(nums)) if i%2 != 0])[::-1]
    even = sorted([nums[i] for i in range(len(nums)) if i%2 == 0])
    for i in range(len(res)):
        if res[i] == 0:
            res[i] = even[0]
            even.pop(0)
        else:
            res[i] = odd[0]
            odd.pop(0)
    return res

#8. https://leetcode.com/problems/path-crossing/description/
def isPathCrossing(self, nums: str) -> bool:
    coor = [0, 0]
    res = [[0, 0]]
    for i in nums:
        if i == 'N': coor[1] += 1
        elif i == 'S': coor[1] -= 1
        elif i == 'E': coor[0] += 1
        elif i == 'W': coor[0] -= 1
        if coor in res: return True
        res.append([i for i in coor])
    return False

#9. https://leetcode.com/problems/first-unique-character-in-a-string/description/
def firstUniqChar(self, s: str) -> int:
    s1 = s
    len1 = len(s)
    res = (0, '')
    for i in s:
        s = s.replace(i, '')
        if len1 - len(s) == 1:
            return s1.find(i)
        len1 = len(s)
    return -1

#10. https://leetcode.com/problems/maximum-score-after-splitting-a-string/description/
def maxScore(self, s: str) -> int:
    maxN = 0
    for i in range(1, len(s)):
        if s[:i].count('0') + s[i:].count('1') > maxN:
            maxN = s[:i].count('0') + s[i:].count('1')
    return maxN