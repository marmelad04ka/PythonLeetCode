from typing import List
#1. https://leetcode.com/problems/baseball-game/description/
def calPoints(self, operations: List[str]) -> int:
    res = []
    for i in operations:
        if i == 'C':
            res.pop(int(len(res) - 1))
        elif i == 'D':
            res.append(int(res[len(res) - 1]) * 2)
        elif i == '+':
            res.append(int(res[len(res) - 1]) + int(res[len(res) - 2]))
        else:
            res.append(int(i))
    return sum(res)

#2. https://leetcode.com/problems/neither-minimum-nor-maximum/description/
def findNonMinOrMax(self, nums: List[int]) -> int:
    nums.sort()
    res = -1
    for i in range(1, len(nums) - 1):
        res = nums[i]
        break
    return res

#3. https://leetcode.com/problems/find-target-indices-after-sorting-array/description/
def targetIndices(self, nums: List[int], target: int) -> List[int]:
    res = []
    nums.sort()
    for i in range(len(nums)):
        if nums[i] == target:
            res.append(i)
    return res

#4. https://leetcode.com/problems/sort-array-by-parity/description/
def sortArrayByParity(self, nums: List[int]) -> List[int]:
    nums.sort(key = lambda x: x%2 != 0)
    return nums

#5. https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/description/
def sumZero(self, n: int) -> List[int]:
    res = []
    for i in range(1, int(n/2) + 1):
        res.append(i)
        res.append(-i)
    if n%2 != 0: res.append(0)
    return res

#6. https://leetcode.com/problems/special-array-i/description/
def isArraySpecial(self, nums: List[int]) -> bool:
    for i in range(len(nums) - 1):
        if nums[i]%2 == 0 and nums[i + 1]%2 == 0 or nums[i]%2 != 0 and nums[i + 1]%2 != 0:
            return False
    return True

#7. https://leetcode.com/problems/robot-return-to-origin/description/
def judgeCircle(self, moves: str) -> bool:
    return moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R')

#8. https://leetcode.com/problems/minimize-string-length/description/
def minimizedStringLength(self, s: str) -> int:
    return len(list(set(s)))

#9.
#10.