from typing import List
#1. https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/
def strStr(self, haystack: str, needle: str) -> int:
    haystack = haystack.replace(needle, '0')
    return haystack.find('0')

#2. https://leetcode.com/problems/repeated-substring-pattern/description/
def repeatedSubstringPattern(self, s: str) -> bool:
    return True if s in (s+s)[1:-1] else False

#3. https://leetcode.com/problems/remove-digit-from-number-to-maximize-result/description/
def removeDigit(self, number: str, digit: str) -> str:
    arr = [i for i in range(0, len(number)) if number[i] == digit]
    result = 0
    for i in arr:
        if int(number[:i] + number[i + 1:]) > result:
            result = int(number[:i] + number[i + 1:])
    return str(result)

#4.
#5.
#6.
#7.
#8.
#9.
#10.