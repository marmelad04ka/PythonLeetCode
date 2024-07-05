from typing import List
#1. https://leetcode.com/problems/number-of-1-bits/description/
def hammingWeight(self, n: int) -> int:
    return bin(n).count('1')

#2. https://leetcode.com/problems/lucky-numbers-in-a-matrix/description/
def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
    minR = [min(i) for i in matrix]
    maxC = [i for i in range(len(matrix) - (len(matrix) - len(matrix[0])))]
    mid = []
    for i in range(len(matrix) - (len(matrix) - len(matrix[0]))):
        for ii in range(len(matrix)):
            mid.append(matrix[ii][i])
        maxC[i] = max(mid)
        mid.clear()
    for i in minR:
        if i in maxC: return [i]
    return []

#3. https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/description/
def checkString(self, s: str) -> bool:
    if 'b' not in s: return True
    indA = 0
    indB = -1
    for i in range(len(s)):
        if s[i] == 'a': indA = i
        if s[i] == 'b' and indB == -1:
            indB = i
    return indB >= indA

#4. https://leetcode.com/problems/fibonacci-number/description/
def fib(self, n: int) -> int:
    if n == 0: return 0
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i - 2] + fib[i - 1])
    return fib[len(fib) - 1] + fib[(len(fib) - 2)]

#5. https://leetcode.com/problems/keep-multiplying-found-values-by-two/description/
def findFinalValue(self, nums: List[int], original: int) -> int:
    count = original
    nums.sort()
    for i in nums:
        if i == count: count *= 2
    return count

#6. https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/description/
def maximumCount(self, nums: List[int]) -> int:
    neg, pos = 0, 0
    for i in nums:
        if i > 0: pos += 1
        if i < 0: neg += 1
    return max(pos, neg)

#7. https://leetcode.com/problems/keyboard-row/description/
def findWords(self, words: List[str]) -> List[str]:
    res = []
    firstRow, secondRow, thirdRow = 'qwertyuiop', 'asdfghjkl', 'zxcvbnm'
    count = [0, 0, 0]
    for i in words:
        for j in i.lower():
            if j in firstRow: count[0] += 1
            if j in secondRow: count[1] += 1
            if j in thirdRow: count[2] += 1
        if count[0] != 0 and count[1] == 0 and count[2] == 0 or count[0] == 0 and count[1] != 0 and count[2] == 0 or count[0] == 0 and count[1] == 0 and count[2] != 0:
            res.append(i)
        count[0] = 0
        count[1] = 0
        count[2] = 0
    return res

#8. https://leetcode.com/problems/sort-array-by-parity-ii/description/
def sortArrayByParityII(self, nums: List[int]) -> List[int]:
    res = []
    odd, even = 1, 0
    for i in nums:
        if i%2 == 0:
            res.insert(even, i)
            even += 2
        else:
            res.insert(odd, i)
            odd += 2
    return res

#9. https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/
def countCharacters(self, words: List[str], chars: str) -> int:
    sumW, count = 0, 0
    strT = chars
    for i in range(len(words)):
        for j in words[i]:
            if j in strT:
                strT = strT[:strT.find(j)] + strT[strT.find(j) + 1:]
                count += 1
        strT = chars
        if count == len(words[i]):
            sumW += len(words[i])
        count = 0
    return sumW

#10.