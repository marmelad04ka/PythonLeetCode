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

#4. https://leetcode.com/problems/replace-all-s-to-avoid-consecutive-repeating-characters/description/

def modifyString(self, s: str) -> str:
    al = 'qwertyuiopasdfghjklzxcvbnm'
    s = '1' + s + '1'
    arr = [i for i in s]
    for i in range(0, len(arr)):
        if arr[i] == '?':
            al = al.replace(arr[i - 1], '')
            al = al.replace(arr[i + 1], '')
            arr[i] = al[0]
            al = 'qwertyuiopasdfghjklzxcvbnm'
    return ''.join(arr)[1:-1]
#5.
#6.
#7.
#8.
#9.
#10.