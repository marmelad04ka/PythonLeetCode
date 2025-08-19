from typing import List
#2535. https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/description/
def differenceOfSum(self, nums: List[int]) -> int:
    res = 0
    for i in range(len(nums)):
        if nums[i] < 10:
            res += nums[i]
        else:
            res += sum(map(int, str(nums[i])))
    return sum(nums) - res

#2194. https://leetcode.com/problems/cells-in-a-range-on-an-excel-sheet/description/
def cellsInRange(self, s: str) -> List[str]:
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    arr = []
    minN = int(min([s[1], s[4]]))
    maxN = int(max([s[1], s[4]]))
    for i in alphabet[alphabet.find(s[0]):alphabet.find(s[3]) + 1]:
        for ii in range(minN, maxN + 1):
            arr.append(i + str(ii))
    return arr

#2485. https://leetcode.com/problems/find-the-pivot-integer/description/
def pivotInteger(self, n: int) -> int:
    arr = [i for i in range(1, n + 1)]
    lS = 0
    rS = sum(arr)
    for i in arr:
        lS += i
        if lS == rS: return i
        rS -= i
    return -1

#2108. https://leetcode.com/problems/find-first-palindromic-string-in-the-array/description/
def firstPalindrome(self, words: List[str]) -> str:
    for i in words:
        if i == i[::-1]:
            return i
    return ""

#2006. https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/description/
def countKDifference(self, nums: List[int], k: int) -> int:
    result = 0
    for i in range(len(nums)):
        for ii in range(i, len(nums)):
            if abs(nums[i] - nums[ii]) == k:
                result += 1
    return result

#2810. https://leetcode.com/problems/faulty-keyboard/description/
def finalString(self, s: str) -> str:
    res = ''
    for i in s:
        if i == 'i':
            res = res[::-1]
            continue
        res += i
    return res

#709. https://leetcode.com/problems/to-lower-case/description/
def toLowerCase(self, s: str) -> str:
    return (s.lower())

#1832. https://leetcode.com/problems/check-if-the-sentence-is-pangram/description/
def checkIfPangram(self, sentence: str) -> bool:
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for i in alphabet:
        if sentence.find(i) == -1:
            return False
    return True

#1732. https://leetcode.com/problems/find-the-highest-altitude/description/
def largestAltitude(self, gain: List[int]) -> int:
    arr = [0, gain[0]]
    for i in range(len(gain) - 1):
        g = gain[i] + gain[i + 1]
        arr.append(g)
        gain[i + 1] = g
    return max(arr)

#1859. https://leetcode.com/problems/sorting-the-sentence/description/
def sortSentence(self, s: str) -> str:
    l1 = s.split(" ")
    arr = [0 for i in range(len(l1))]
    for i in l1:
        ind = int(''.join((item for item in i if item.isdigit()))) - 1
        item = ''.join((item for item in i if not item.isdigit()))
        arr[ind] = item
    return ' '.join(arr)
