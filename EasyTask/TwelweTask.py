from typing import List
#1. https://leetcode.com/problems/maximum-number-of-pairs-in-array/description/
def numberOfPairs(self, nums: List[int]) -> List[int]:
    uniq = list(set(nums))
    res = [0, 0]
    for i in uniq:
        count = nums.count(i)
        if count % 2 == 0:
            res[0] += int(count / 2)
        elif count % 2 != 0 and count > 1:
            res[0] += int(count / 2)
            res[1] += 1
        else:
            res[1] += 1
    return res

#2. https://leetcode.com/problems/minimum-time-to-type-word-using-special-typewriter/description/
def minTimeToType(self, word: str) -> int:
    res = len(word)
    if word[0] != 'a': word = 'a' + word
    for i in range(len(word) - 1):
        go = abs(ord(word[i]) - ord(word[i + 1]))
        back = (26 - max(ord(word[i]), ord(word[i + 1])) + min(ord(word[i]), ord(word[i + 1])))
        res += min(go, back)
    return res

#3. https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/description/
def findMaxK(self, nums: List[int]) -> int:
    res = 0
    minus = [i for i in nums if i < 0]
    minus.sort()
    plus = [i for i in nums if i > 0]
    plus.sort()
    for i in plus[::-1]:
        if minus.count(-i) > 0:
            res = i
            break
    return res

#4. https://leetcode.com/problems/ant-on-the-boundary/description/
def returnToBoundaryCount(self, nums: List[int]) -> int:
    res = 0
    mid = 0
    for i in range(len(nums)):
        mid += nums[i]
        if mid == 0:
            res += 1
    return res

#5. https://leetcode.com/problems/relative-sort-array/description/
def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
    res = []
    for i in arr2:
        n = arr1.count(i)
        res += [i] * n
    arr1.sort()
    for i in arr1:
        if i not in arr2:
            res.append(i)
    return res

#6.
#7.
#8.
#9.
#10.