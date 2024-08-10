from typing import List
#1. https://leetcode.com/problems/find-the-k-beauty-of-a-number/description/
def divisorSubstrings(self, num: int, k: int) -> int:
    sN = str(num)
    count = 0
    for i in range(len(sN)):
        if len(sN[i:i + k]) < k: break
        if int(sN[i:i + k]) != 0:
            if num % int(sN[i:i + k]) == 0: count += 1
        else:
            continue
    return count

#2. https://leetcode.com/problems/max-consecutive-ones/description/
def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    arr = []
    count = 0
    for i in nums:
        if i == 1: count += 1
        else:
            arr.append(count)
            count = 0
    arr.append(count)
    return max(arr)

#3. https://leetcode.com/problems/find-the-difference/description/
def findTheDifference(self, s: str, t: str) -> str:
    s = sorted(s)
    t = sorted(t)
    for i in range(len(t)):
        if i == len(t) - 1 or t[i] != s[i]: return t[i]

#4. https://leetcode.com/problems/count-elements-with-strictly-smaller-and-greater-elements/description/
def countElements(self, nums: List[int]) -> int:
    maxN, minN, count = max(nums), min(nums), 0
    for i in nums:
        if i != minN and i != maxN: count += 1
    return count

#5.
#6.
#7.
#8.
#9.
#10.