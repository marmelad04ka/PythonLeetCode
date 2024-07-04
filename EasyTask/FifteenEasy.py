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
#4.
#5.
#6.
#7.
#8.
#9.
#10.