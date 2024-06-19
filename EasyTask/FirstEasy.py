from typing import List
#1. https://leetcode.com/problems/score-of-a-string/description/
def scoreOfString(self, s: str) -> int:
    res = 0
    for i in range(len(s) - 1):
        res += abs(ord(s[i]) - ord(s[i + 1]))
    return res

#2. https://leetcode.com/problems/find-the-maximum-achievable-number/
def theMaximumAchievableX(self, num: int, t: int) -> int:
    return num + t + t

#3. https://leetcode.com/problems/concatenation-of-array/description/
def getConcatenation(self, nums: List[int]) -> List[int]:
    return nums + 1

#4. https://leetcode.com/problems/build-array-from-permutation/description/
def buildArray(self, nums: List[int]) -> List[int]:
    res = []
    for i in range(len(nums)):
        res.append(nums[nums[i]])
    return res
#5. https://leetcode.com/problems/permutation-difference-between-two-strings/description/
def findPermutationDifference(self, s: str, t: str):
    res = 0
    for i in range(len(s)):
        res += abs(s.find(s[i]) - t.find(s[i]))
    return res

#6. https://leetcode.com/problems/convert-the-temperature/description/
def convertTemperature(self, celsius: float):
    res = []
    k = celsius + 273.15
    f = celsius * 1.80 + 32.00
    res.append(k)
    res.append(f)
    return res

#7. https://leetcode.com/problems/defanging-an-ip-address/description/
def defangIPaddr(self, address: str):
    return address.replace('.', '[.]')

#8. https://leetcode.com/problems/final-value-of-variable-after-performing-operations/description/
def finalValueAfterOperations(self, operations: List[str]) -> int:
    res = 0
    for i in operations:
        if i[1] == "-": res -= 1
        else: res += 1
    return res

#9. https://leetcode.com/problems/number-of-good-pairs/description/
def numIdenticalPairs(self, nums: List[int]) -> int:
    res = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                res += 1
    return res

#10. https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/
def differenceOfSums(self, n: int, m: int) -> int:
        nonDi = sum(i for i in range(1, n+1) if i % m != 0)
        Di = sum(i for i in range(1, n+1) if i % m == 0)
        return nonDi - Di