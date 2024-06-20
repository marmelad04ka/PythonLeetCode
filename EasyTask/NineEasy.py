from typing import List
#1. https://leetcode.com/problems/counting-bits/description/
def countBits(self, n: int) -> List[int]:
    res = []
    for i in range(0, n + 1):
        res.append(str(bin(i)).count('1'))
    return res

#2. https://leetcode.com/problems/unique-number-of-occurrences/description/
def uniqueOccurrences(self, arr: List[int]) -> bool:
    dir = {}
    res = []
    for i in arr:
        if i in dir:
            dir[i] += 1
        else:
            dir[i] = 1
    for key in dir.keys():
        res.append(dir.get(key))
    return len(res) == len(list(set(res)))
#3. https://leetcode.com/problems/roman-to-integer/description/
def romanToInt(self, s: str) -> int:
    dir = {'I': 1,'IV': 4, 'V': 5, 'IX': 9,
          'X': 10, 'XL': 40, 'L': 50, 'XC': 90,
          'C': 100, 'CD': 400, 'D': 500, 'CM': 900,
          'M': 1000}
    res = s.count('IV') * 4 + s.count('IX') * 9 + s.count('XL') * 40 + s.count('XC') * 90 + s.count('CD') * 400 + s.count('CM') * 900
    s = s.replace("IV", "").replace("IX", "").replace("XL", "").replace("XC", "").replace("CD", "").replace("CM", "")
    l1 = list(s)
    for i in range(len(l1)):
        if dir.get(l1[i]):
            res += dir[l1[i]]
    return res

#4. https://leetcode.com/problems/find-pivot-index/description/
def pivotIndex(self, nums: List[int]) -> int:
    left_sum, total_sum = 0, sum(nums)
    for i, n in enumerate(nums):
        right_sum = total_sum - left_sum - n
        if left_sum == right_sum:
            return i
        left_sum += n
    return -1

#5. https://leetcode.com/problems/reverse-vowels-of-a-string/
def reverseVowels(self, s: str) -> str:
    l1 = list(s)
    onlyA = [i for i in s if i in 'aeiouAEIOU'][::-1]
    for i in range(len(l1)):
        if l1[i] in 'aeiouAEIOU':
            l1[i] = onlyA[0]
            onlyA.pop(0)
    return ''.join(l1)

#6.
#7.
#8.
#9.
#10.