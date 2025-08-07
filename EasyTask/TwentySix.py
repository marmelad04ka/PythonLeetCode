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

#5. https://leetcode.com/problems/account-balance-after-rounded-purchase/description/
def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
    return  100 - (purchaseAmount + 10 - purchaseAmount%10) if purchaseAmount%10 >= 5 else 100 - (purchaseAmount - purchaseAmount%10)

#6. https://leetcode.com/problems/form-smallest-number-from-two-digit-arrays/description/
def minNumber(self, nums1: List[int], nums2: List[int]) -> int:

    for i in range(1, 10):
        if i in nums1 and i in nums2: return i
    nums1.sort()
    nums2.sort()
    res = str(nums1[0]) + str(nums2[0])
    return int(res) if int(res) < int(res[::-1]) else int(res[::-1])

#7. https://leetcode.com/problems/longest-palindrome/description/
def longestPalindrome(self, s: str) -> int:
    result = 0
    count = 0
    arr = [s.count(i) for i in set(s)]
    for i in arr:
        if i%2 != 0 and count == 0:
            count += 1
            result += i
            continue
        if i%2 == 0:
            result += i
        else:
            result += i - 1
    return result

#8. https://leetcode.com/problems/transform-array-by-parity/description/
def transformArray(self, nums: List[int]) -> List[int]:
    result = []
    for i in nums:
        if i % 2 == 0:
            result.append(0)
        else:
            result.append(1)
    result.sort()
    return result

#9. https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description/
def getSneakyNumbers(self, nums: List[int]) -> List[int]:
    result = []
    zn = [0 for i in range(max(nums) + 1)]
    for i in nums:
        zn[i] += 1
        if zn[i] == 2:
            result.append(i)
    return result

#10. https://leetcode.com/problems/count-the-number-of-consistent-strings/description/
def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
    allowed_set = set(allowed)
    return sum(1 for word in words if all(char in allowed_set for char in word))