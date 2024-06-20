from typing import List
#1. https://leetcode.com/problems/replace-all-digits-with-characters/description/
def replaceDigits(self, s: str) -> str:
    res = ''
    for i in range(len(s)):
        if '0' <= s[i] <= '9':
            res += chr(ord(s[i - 1]) + int(s[i]))
        else:
            res += s[i]
    return res

#2. https://leetcode.com/problems/find-maximum-number-of-string-pairs/description/
def maximumNumberOfStringPairs(self, words: List[str]) -> int:
    res = 0
    for i in range(len(words)):
        for ii in range(i + 1, len(words)):
            if words[i] == words[ii] or words[i] == words[ii][::-1]:
                res += 1
    return res

#3. https://leetcode.com/problems/sum-of-squares-of-special-elements/description/
def sumOfSquares(self, nums: List[int]) -> int:
    res = 0
    for i in range(1, len(nums) + 1):
        if len(nums)%i == 0:
            res += nums[i - 1] ** 2
    return res

#4. https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/description/
def numOfStrings(self, patterns: List[str], word: str) -> int:
    res = 0
    for i in patterns:
        if word.count(i) > 0:
            res += 1
    return res

#5. https://leetcode.com/problems/rings-and-rods/description/
def countPoints(self, rings: str) -> int:
    res = 0
    arr1 = [[], [], [], [], [], [], [], [] ,[], []]
    l1 = [rings[i:i+2] for i in range(0, len(rings), 2)]
    for i in range(len(l1)):
        arr1[int(l1[i][1])] += l1[i]
    for i in arr1:
        if i.count('R') > 0 and i.count('B') > 0 and i.count('G') > 0: res += 1
    return res

#6. https://leetcode.com/problems/height-checker/description/
def heightChecker(self, heights: List[int]) -> int:
    arr1 = [i for i in heights]
    arr1.sort()
    res = 0
    for i in range(len(heights)):
        if heights[i] != arr1[i]: res += 1
    return res

#7. https://leetcode.com/problems/number-of-changing-keys/description/
def countKeyChanges(self, s: str) -> int:
    res = 0
    for i in range(1, len(s)):
        if s[i].lower() != s[i - 1].lower(): res += 1
    return res

#8. https://leetcode.com/problems/sort-the-people/description/
def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
    res = []
    i = 0
    while i != 1:
        ind = heights.index(max(heights))
        res.append(names[ind])
        heights[ind] = 0
        if sum(heights) == 0: break
    return res

#9. https://leetcode.com/problems/merge-strings-alternately/description/
def mergeAlternately(self, word1: str, word2: str) -> str:
    res = ''
    for i in range(len(word1)):
        res += word1[i]
        if i > len(word2) - 1: continue
        res += word2[i]
    if len(word2) > len(word1):
        res += word2[len(word1):]
    return res

#10. https://leetcode.com/problems/a-number-after-a-double-reversal/description/
def isSameAfterReversals(self, num: int) -> bool:
    return False if num%10 == 0 and num != 0 else True
