from typing import List
#1. https://leetcode.com/problems/count-pairs-of-similar-strings/description/
def similarPairs(self, words: List[str]) -> int:
    n1 = [sorted(''.join(set(i))) for i in words]
    res = 0
    for i in range(len(n1)):
        for j in range(i + 1, len(n1)):
            if n1[i] == n1[j]: res += 1
    return res

#2. https://leetcode.com/problems/greatest-english-letter-in-upper-and-lower-case/description/
def greatestLetter(self, s: str) -> str:
    s1 = list(set(s))
    res = []
    for i in s1:
        if i.lower() in s and i.upper() in s: res += i.upper()
    if len(res) == 0: return ""
    return sorted(res)[::-1][0]

#3. https://leetcode.com/problems/time-needed-to-buy-tickets/description/
def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
    sumT = 0
    while True:
        for i in range(len(tickets)):
            if tickets[k] == 0: break
            if tickets[i] == 0: continue
            tickets[i] -= 1
            sumT += 1
        if tickets[k] == 0: break
    return sumT

#4. https://leetcode.com/problems/find-the-array-concatenation-value/description/
def findTheArrayConcVal(self, nums: List[int]) -> int:
    sumAll = 0
    for i in range(int(len(nums)/2)):
        sumAll += int(str(nums[i]) + str(nums[len(nums)-(i+1)]))
    if len(nums)%2 != 0: sumAll += nums[int(len(nums)/2)]
    return sumAll

#5. https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/description/
def simple_number(n):
    if n == 2: return True
    if n%2 == 0 or n <= 1: return False
    for i in range(3, int(n * 0.5) + 1, 2):
        if n%i == 0: return False
    return True
def countPrimeSetBits(self, left: int, right: int) -> int:
    result = 0
    for i in range(left, right + 1):
        if simple_number(i.bit_count()): result += 1
    return result

#6. https://leetcode.com/problems/check-if-numbers-are-ascending-in-a-sentence/description/
def areNumbersAscending(self, s: str) -> bool:
    result = 0
    count = 0
    for i in s.split(" "):
        if i.isdigit():
            if count > 0 and result >= int(i): return False
            result = int(i)
            count += 1
    return True

#7. https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/description/
def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
    arr.sort()
    for i in range(len(arr) - 1):
        if arr[i] + (arr[1] - arr[0]) != arr[i + 1]: return False
    return True

#8. https://leetcode.com/problems/minimum-string-length-after-removing-substrings/description/
def minLength(self, s: str) -> int:
    s1 = s
    while True:
        newS = s1
        s1 = s1.replace('AB', "")
        s1 = s1.replace('CD', "")
        if newS == s1: break
    return len(s1)

#9. https://leetcode.com/problems/find-the-encrypted-string/description/
def getEncryptedString(self, s: str, k: int) -> str:
    n = k%len(s)
    res = ''
    for i in range(len(s)):
        if i + 1 + n > len(s):
            res += s[(i + n) - len(s)]
        else: res += s[i + n]
    return res

#10. https://leetcode.com/problems/palindrome-number/description/
def isPalindrome(self, x: int) -> bool:
    strX = list(str(x))[::-1]
    return str(x) == ''.join(strX)