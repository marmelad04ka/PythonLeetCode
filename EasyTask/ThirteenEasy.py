import math
from typing import List
#1. https://leetcode.com/problems/percentage-of-letter-in-string/description/
def percentageLetter(self, s: str, letter: str) -> int:
    return math.floor((s.count(letter) * 100) / len(s))

#2. https://leetcode.com/problems/split-strings-by-separator/description/
def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
    res = []
    str1 = separator.join(words)
    for i in str1.split(separator):
        if i == "":continue
        res.append(i)
    return res

#3. https://leetcode.com/problems/single-number/description/
def singleNumber(self, nums: List[int]) -> int:
    nums.sort()
    nums += 'a'
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1] or nums[i] == nums[i - 1]:
            continue
        else:
            return nums[i]

#4. https://leetcode.com/problems/maximum-number-of-balls-in-a-box/description/
def sumOfDigit(num):
    res = 0
    while num > 0:
        res += num%10
        num = num//10
    return res
def countBalls(self, lowLimit: int, highLimit: int) -> int:
    dir = {}
    for i in range(lowLimit, highLimit + 1):
        if sumOfDigit(i) in dir:
            dir[sumOfDigit(i)] +=1
        else: dir[sumOfDigit(i)] = 1
    sorted_dir = sorted(dir.items(), key=lambda item: item[1])
    return sorted_dir[len(sorted_dir) - 1][1]

#5. https://leetcode.com/problems/divide-array-into-equal-pairs/description/
def divideArray(self, nums: List[int]) -> bool:
    res = 1
    nums.sort()
    nums += 'a'
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]: res += 1
        elif res%2 != 0: return False
        else: res = 1
    return True

#6. https://leetcode.com/problems/maximum-number-of-words-you-can-type/description/
def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
    res, mid = 0, 0
    text += ' 1'
    for i in text.split(" "):
        if mid > 0:
            res += 1
            mid = 0
        for ii in brokenLetters:
            if ii in i:
                mid += 1
    return len(text.split(" ")) - 1 - res

#7.
#8.
#9.
#10.