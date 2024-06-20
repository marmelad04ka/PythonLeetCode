from typing import List
import math
#1. https://leetcode.com/problems/reverse-words-in-a-string-iii/description/
def reverseWords(self, s: str) -> str:
    result = ""
    for i in s.split(" "):
        result += i[::-1] + " "
    return result.strip()

#2. https://leetcode.com/problems/harshad-number/description/
def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
    mid = x
    b = []
    while mid > 0:
        b.append(mid % 10)
        mid = mid // 10
    return sum(b) if x%(sum(b)) == 0 else -1

#3. https://leetcode.com/problems/check-if-a-string-is-an-acronym-of-words/description/
def isAcronym(self, words: List[str], s: str) -> bool:
    if len(words) != len(s): return False
    count = 0
    for i in words:
        if i[0] != s[count]: return False
        count += 1
    return True

#4. https://leetcode.com/problems/matrix-diagonal-sum/description/
def diagonalSum(self, mat: List[List[int]]) -> int:
    result = 0
    for i in range(len(mat)):
        result += mat[i][i] + mat[i][len(mat) - (i + 1)]
    return result if len(mat)%2 == 0 else result - mat[int(len(mat)/2)][int(len(mat[int(len(mat)/2)])/2)]

#5. https://leetcode.com/problems/unique-morse-code-words/description/
def uniqueMorseRepresentations(self, words: List[str]) -> int:
    morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    arrMorse = []
    for i in range(len(words)):
        l1 = list(words[i])
        m = ''
        for ii in range(len(l1)):
            m += morse[alphabet.find(l1[ii])]
        arrMorse.append(m)
    return  len(list(set(arrMorse)))

#6. https://leetcode.com/problems/maximum-product-difference-between-two-pairs/description/
def maxProductDifference(self, nums: List[int]) -> int:
    nums.sort()
    len1 = len(nums)
    return (nums[len1 - 1] * nums[len1 - 2]) - (nums[0] * nums[1])

#7. https://leetcode.com/problems/maximum-69-number/description/
def maximum69Number (self, num: int) -> int:
    l1 = list(str(num))
    l1[str(num).find("6")] = '9'
    return int(''.join(l1))

#8. https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/description/
def maximizeSum(self, nums: List[int], k: int) -> int:
    result = 0
    max_nums = max(nums)
    for i in range(max_nums, max_nums + k):
        result += i
    return result

#9. https://leetcode.com/problems/flipping-an-image/description/
def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
    res = []
    for i in image:
        for ii in range(len(i)):
            if i[ii] == 0:
                i[ii] = 1
            else: i[ii] = 0
        res.append(i[::-1])
    return res

#10. https://leetcode.com/problems/lexicographically-smallest-palindrome/description/
def makeSmallestPalindrome(self, s: str) -> str:
    res = [0 for i in range(1, len(s) + 1)]
    lenS = len(s) - 1
    for i in range(math.ceil(len(s) / 2)):
        if s[i] == s[lenS - i]:
            res[i] = s[i]
            res[lenS - i] = s[lenS - i]
        elif s[i] < s[lenS - i]:
            res[i] = s[i]
            res[lenS - i] = s[i]
        else:
            res[i] = s[lenS - i]
            res[lenS - i] = s[lenS - i]
    return ''.join(res)
