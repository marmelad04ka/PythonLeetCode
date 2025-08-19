#504. https://leetcode.com/problems/base-7/description/
from typing import List


def convertToBase7(self, num: int) -> str:
    if num == 0: return '0'
    flag = 0
    if num < 0:
        flag = 1
        num *= -1
    result = ''
    while num > 0:
        result += str(num - (num // 7 * 7))
        num = num // 7
    return result[::-1] if flag == 0 else '-' + result[::-1]

#645. https://leetcode.com/problems/set-mismatch/description/
def findErrorNums(self, nums: List[int]) -> List[int]:
    result = [0, 0]
    set_n_sum = sum(set(nums))
    result[0] = abs(set_n_sum - sum(nums))
    result[1] = abs(set_n_sum - sum([i for i in range(max(nums)+1)]))
    if result[1] == 0: result[1] = max(nums) + 1
    return result

#744. https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/
def nextGreatestLetter(self, letters: List[str], target: str) -> str:
    for ch in letters:
        if ch > target:
            return ch
    return letters[0]

#1.
#1.
#1.
#1.
#1.
#1.
#1.