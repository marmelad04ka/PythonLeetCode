from typing import List
#1. https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/description/
def freqAlphabets(self, s: str) -> str:
    alphabet = '0abcdefghijklmnopqrstuvwxyz'
    l1 = list(s)
    res = ''
    for i in range(len(l1)):
        if l1[i] == '#':
            l1[i] = l1[i - 2] + l1[i - 1]
            l1[i - 2] = ''
            l1[i - 1] = ''
    for i in range(len(l1)):
        if l1[i] == '': continue
        res += alphabet[int(l1[i])]
    return res

#2. https://leetcode.com/problems/count-pairs-that-form-a-complete-day-i/description/
def countCompleteDayPairs(self, hours: List[int]) -> int:
    res = 0
    for i in range(len(hours)):
        for ii in range(i + 1, len(hours)):
            if (hours[i] + hours[ii])%24 == 0:
                res += 1
    return res

#3. https://leetcode.com/problems/separate-the-digits-in-an-array/description/
def separateDigits(self, nums: List[int]) -> List[int]:
    res = []
    for i in range(len(nums)):
        b = []
        while nums[i] > 0:
            b.append(nums[i] % 10)
            nums[i] = nums[i] // 10
        b = b[::-1]
        for ii in range(len(b)):
            res.append(b[ii])
    return res

#4. https://leetcode.com/problems/count-elements-with-maximum-frequency/description/
def maxFrequencyElements(self, nums: List[int]) -> int:
    dir = {}
    for i in nums:
        if i in dir:
            dir[i] += 1
        else:
            dir[i] = 1
    arr1 = [dir.get(i) for i in dir]
    arr1.sort()
    return arr1.count(max(arr1)) * max(arr1)

#5. https://leetcode.com/problems/number-of-common-factors/description/
def commonFactors(self, a: int, b: int) -> int:
    res = 0
    for i in range(1, b + 1):
        if a%i == 0 and b%i == 0:res += 1
    return res

#6. https://leetcode.com/problems/reverse-string/description/
def reverseString(self, s: List[str]) -> None:
    s.reverse()

#7. https://leetcode.com/problems/self-dividing-numbers/description/
def selfDividingNumbers(self, left: int, right: int) -> List[int]:
    res = []
    mid = 0
    for i in range(left, right + 1):
        a = i
        b = []
        while a > 0:
            b.append(a % 10)
            a = a // 10
        for ii in range(len(b)):
            if b[ii] == 0: break
            if i%b[ii] == 0:
                mid += 1
        if mid == len(b): res.append(i)
        mid = 0
    return res

#8. https://leetcode.com/problems/determine-if-string-halves-are-alike/description/
def halvesAreAlike(self, s: str) -> bool:
    firstH = 0
    lenS = int(len(s)/2)
    for i in range(len(s)):
        if i < lenS and s[i] in 'aeiouAEIOU': firstH += 1
        elif s[i] in 'aeiouAEIOU': firstH -= 1
    return firstH == 0

#9. https://leetcode.com/problems/remove-trailing-zeros-from-a-string/description/
def removeTrailingZeros(self, num: str) -> str:
    return str(int(num[::-1]))[::-1]

#10. https://leetcode.com/problems/calculate-delayed-arrival-time/description/
def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
    return (arrivalTime + delayedTime)%24