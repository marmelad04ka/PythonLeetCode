#58. https://leetcode.com/problems/length-of-last-word/description/
from typing import List


def lengthOfLastWord(self, s: str) -> int:
    return len(s.split()[-1])

#67. https://leetcode.com/problems/add-binary/description/
def addBinary(self, a: str, b: str) -> str:
    return bin(int(a, 2) + int(b, 2))[2:]

#70. https://leetcode.com/problems/climbing-stairs/description/
def climbStairs(self, n: int) -> int:
    first, second = 1, 2
    if n <= 2: return n
    for i in range(n - 2):
        second += first
        first = second - first
    return second

#125. https://leetcode.com/problems/valid-palindrome/description/
def isPalindrome(self, s: str) -> bool:
    alph_s = ''
    for i in s.lower():
        if i in 'qwertyuiopasdfghjklzxcvbnm0123456789':
            alph_s += i
    return alph_s == alph_s[::-1]

#190. https://leetcode.com/problems/reverse-bits/description/
def reverseBits(self, n: int) -> int:
    binary = bin(n)[2:]
    padded = binary.zfill(32)
    reversed_binary = padded[::-1]
    return int(reversed_binary, 2)

#217. https://leetcode.com/problems/contains-duplicate/description/
def containsDuplicate(self, nums: List[int]) -> bool:
    seen = set()
    for x in nums:
        if x in seen:
            return True
        seen.add(x)
    return False

#231. https://leetcode.com/problems/power-of-two/description/
def isPowerOfTwo(self, n: int) -> bool:
    return n > 0 and (n & (n - 1)) == 0

#1. https://leetcode.com/problems/two-sum/description/
def twoSum(self, nums: List[int], target: int) -> List[int]:
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

#2264. https://leetcode.com/problems/largest-3-same-digit-number-in-string/description/
def largestGoodInteger(self, num: str) -> str:
    result = ''
    for i in range(len(num) - 2):
        substring = num[i:i+3]
        if substring[0] == substring[1] == substring[2]:
            if substring > result: result = substring
    return result
#1.