from typing import List
#1. https://leetcode.com/problems/squares-of-a-sorted-array/description/
def sortedSquares(self, nums: List[int]) -> List[int]:
    return sorted([i * i for i in nums])

#2. https://leetcode.com/problems/count-prefixes-of-a-given-string/description/
def countPrefixes(self, words: List[str], s: str) -> int:
    result = 0
    for i in words:
        if i in s[:len(i)]:
            result += 1
    return result

#3. https://leetcode.com/problems/fizz-buzz/description/
def fizzBuzz(self, n: int) -> List[str]:
    res = []
    for i in range(1, n + 1):
        if i%3 == 0 and i%5 == 0: res.append('FizzBuzz')
        elif i%5 == 0: res.append("Buzz")
        elif i%3 == 0: res.append('Fizz')
        else: res.append(str(i))
    return res

#4. https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/description/
def minimumOperations(self, nums: List[int]) -> int:
    return len(set(nums)) if 0 not in nums else len(set(nums))-1

#5. https://leetcode.com/problems/find-common-characters/description/
def commonChars(self, words: List[str]) -> List[str]:
    res = []
    count = 0
    for i in words[0]:
        for ii in range(1, len(words)):
            if i in words[ii]:
                words[ii] = words[ii].replace(i, '', 1)
                count += 1
        if count == len(words) - 1: res.append(i)
        count = 0
    return res

#6. https://leetcode.com/problems/maximum-value-of-a-string-in-an-array/description/
def maximumValue(self, strs: List[str]) -> int:
    res = []
    for i in strs:
        try:
            res.append(int(i))
        except ValueError: res.append(len(i))
    return max(res)

#7. https://leetcode.com/problems/check-if-number-has-equal-digit-count-and-digit-value/description/
def digitCount(self, num: str) -> bool:
    for i in range(len(num)):
        if int(num[i]) != num.count(str(i)): return False
    return True

#8. https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays/description/
def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
    return sorted(target) == sorted(arr)

#9.
#10.