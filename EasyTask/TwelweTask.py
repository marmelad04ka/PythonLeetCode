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

#6. https://leetcode.com/problems/intersection-of-two-arrays/description/
def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    nums1 = set(nums1)
    nums2 = set(nums2)
    res = []
    for i in nums1:
        if i in nums2:
            res.append(i)
    return res

#7. https://leetcode.com/problems/pascals-triangle/description/
def generate(self, numRows: int) -> List[List[int]]:
    if numRows == 1: return [[1]]
    res = [[1],[1,1]]
    k = 1
    while numRows > 2:
        mid = [1]
        for i in range(len(res[k]) - 1):
            mid.append(res[k][i] + res[k][i + 1])
        mid.append(1)
        res.append(mid)
        k += 1
        numRows -= 1
    return res

#8. https://leetcode.com/problems/find-the-k-or-of-an-array/description/
def findKOr(self, nums: List[int], k: int) -> int:
    res = ''
    dir = {}
    for i in range(len(nums)):
        binStr = bin(nums[i])[:1:-1]
        for ii in range(len(binStr)):
            if ii in dir:
                dir[ii] += int(binStr[ii])
            else:
                dir[ii] = int(binStr[ii])
    for value in dir.keys():
            if dir[value] >= k:
                res += '1'
            else: res += '0'
    return int(res[::-1], 2)

#9. https://leetcode.com/problems/count-operations-to-obtain-zero/description/
def countOperations(self, num1: int, num2: int) -> int:
    if num1 == 0 or num2 == 0: return 0
    res = 0
    while True:
        if num1 == 0 or num2 == 0:
            break
        if num1 < num2:
            num2 -= num1
        else:
            num1 -= num2
        res += 1
    return res

#10. https://leetcode.com/problems/count-symmetric-integers/description/
def countSymmetricIntegers(self, low: int, high: int) -> int:
    res = 0
    for i in range(low, high + 1):
        if len(str(i))%2 != 0: continue
        l = int(len(str(i))/2)
        if sum(map(int, str(i)[:l])) == sum(map(int, str(i)[l:])):
            res += 1
    return res