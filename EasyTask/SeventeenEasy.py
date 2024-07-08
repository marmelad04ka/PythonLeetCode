from typing import List
#1. https://leetcode.com/problems/number-of-lines-to-write-string/description/
def numberOfLines(self, widths: List[int], s: str) -> List[int]:
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    sumS = 0
    count = 1
    for i in s:
        if sumS + widths[alphabet.index(i)] > 100:
            sumS = 0
            count += 1
            sumS += widths[alphabet.index(i)]
        else:
            sumS += widths[alphabet.index(i)]
    return [count, sumS]

#2. https://leetcode.com/problems/largest-3-same-digit-number-in-string/description/
def largestGoodInteger(self, num: str) -> str:
    for i in range(9, -1, -1):
        if str(i) * 3 in num: return str(i) * 3
    return ''

#3. https://leetcode.com/problems/largest-substring-between-two-equal-characters/description/
def maxLengthBetweenEqualCharacters(self, s: str) -> int:
    res = -1
    for i in range(len(s)):
        sF = s.rfind(s[i])
        if sF != -1 and sF != i:
            count = len(s[i + 1:sF])
            if count > res: res = count
    return res

#4. https://leetcode.com/problems/mean-of-array-after-removing-some-elements/description/
def trimMean(self, arr: List[int]) -> float:
    arr.sort()
    fivePro = int(len(arr) * 0.05)
    sumN = 0
    for i in range(fivePro, len(arr) - fivePro):
        sumN += arr[i]
    return round(sumN/(len(arr) - (fivePro * 2)), 5)

#5. https://leetcode.com/problems/find-the-distance-value-between-two-arrays/description/
def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
    result = len(arr1)
    for i in arr1:
        for ii in arr2:
            if abs(i - ii) <= d:
                result -= 1
                break
    return result
#6. https://leetcode.com/problems/modify-the-matrix/description/
def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
    maxNC = []
    count = 0
    for i in range(len(matrix)- (len(matrix) - len(matrix[0]))):
        for ii in range(len(matrix)):
            if matrix[ii][i] > count: count = matrix[ii][i]
        maxNC.append(count)
        count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] < 0: matrix[i][j] = maxNC[j]
    return matrix

#7.
#8.
#9.
#10.