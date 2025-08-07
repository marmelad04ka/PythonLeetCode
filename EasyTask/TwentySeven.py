#1. https://leetcode.com/problems/convert-date-to-binary/description/
from typing import List


def convertDateToBinary(self, date: str) -> str:
    year, month, day = date.split("-")
    return f"{bin(int(year))[2:]}-{bin(int(month))[2:]}-{bin(int(day))[2:]}"

#2. https://leetcode.com/problems/reverse-degree-of-a-string/description/
def reverseDegree(self, s: str) -> int:
    result = 0
    for i, char in enumerate(s):
        reverse_alphabet_value = ord('z') - ord(char) + 1
        result += reverse_alphabet_value * (i + 1)
    return result

#3. https://leetcode.com/problems/minimum-bit-flips-to-convert-number/description/
def minBitFlips(self, start: int, goal: int) -> int:
    result = 0
    start_m = bin(start)[2:]
    goal_m = bin(goal)[2:]

    max_len = max(len(start_m), len(goal_m))

    start_m = start_m.zfill(max_len)
    goal_m = goal_m.zfill(max_len)

    for i, char in enumerate(start_m):
         if char != goal_m[i]: result += 1
    return result

#4. https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/description/
def maxFreqSum(self, s: str) -> int:
    num_v = 0
    num_c = 0
    arr_a = [0 for i in range(26)]
    for char in s:
        arr_a[ord(char) - 97] += 1
    for index, num in enumerate(arr_a):
        if index in (0, 4, 8, 14, 20):
            if num_v <= num:
                num_v = num
        else:
            if num_c <= num:
                num_c = num
    return num_v + num_c

#5. https://leetcode.com/problems/minimum-operations-to-make-array-sum-divisible-by-k/description/
def minOperations(self, nums: List[int], k: int) -> int:
    total = sum(nums)
    result = total % k
    return result

#6. https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-i/description/
def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
    for i in range(k):
        nums[nums.index(min(nums))] *= multiplier
    return nums

#7. https://leetcode.com/problems/count-items-matching-a-rule/description/
def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
    result = 0
    key_to_index = {"type": 0, "color": 1, "name": 2}
    idx = key_to_index[ruleKey]
    for i in items:
        if i[idx] == ruleValue: result += 1
    return result

#8. https://leetcode.com/problems/minimum-average-of-smallest-and-largest-elements/description/
def minimumAverage(self, nums: List[int]) -> float:
    arr = []
    len_nums = len(nums)
    nums.sort()
    for i in range(int(len_nums/2)):
        arr.append((nums[i] + nums[len_nums - i - 1])/2)
    return min(arr)

#9. https://leetcode.com/problems/find-missing-and-repeated-values/description/
def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
    result = [0, 0]
    flag, sum_l, sum_g, min_l, max_l = 0, 0, 0, grid[0][0], grid[0][0]
    line = []
    for i in grid:
        for j in i:
            if min_l > j:
                min_l = j
            if max_l < j:
                max_l = j
            if j not in line:
                sum_g += j
                line.append(j)
            elif j in line and flag != 1:
                result[0] = j
                flag = 1
    sum_l = (min_l + max_l) * (max_l - min_l + 1) // 2
    if min_l != 1:
        result[1] = min_l - 1
    elif sum_g - sum_l == 0:
        result[1] = max_l + 1
    else:
        result[1] = sum_l - sum_g
    return result

#10. https://leetcode.com/problems/find-common-elements-between-two-arrays/description/
def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
    result = [0, 0]
    small_n = []
    for i in nums1:
        if i in nums2:
            result[0] += 1
            small_n.append(i)
    for i in nums2:
        if i in small_n:
            result[1] += 1
    return result