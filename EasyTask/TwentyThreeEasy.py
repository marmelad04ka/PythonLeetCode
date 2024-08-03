from typing import List
#1. https://leetcode.com/problems/sqrtx/description/
def mySqrt(self, x: int) -> int:
    if x == 1: return 1
    for i in range(0, int(x / 2) + 1):
        if i * i == x:
            return i
        elif i * i > x:
            return i - 1
    return int(x / 2)

#2. https://leetcode.com/problems/largest-number-after-digit-swaps-by-parity/description/
def largestInteger(self, num: int) -> int:
    res = [0 if int(i)%2 == 0 else 1 for i in str(num)]
    odd = sorted([int(i) for i in str(num) if int(i)%2 != 0])[::-1]
    even = sorted([int(i) for i in str(num) if int(i)%2 == 0])[::-1]

    for i in range(len(res)):
        if res[i] == 0:
            res[i] = even[0]
            even.pop(0)
        else:
            res[i] = odd[0]
            odd.pop(0)
    return int(''.join(map(str, res)))

#3. https://leetcode.com/problems/monotonic-array/description/
def isMonotonic(self, nums: List[int]) -> bool:
    count = 1
    for i in range(1, len(nums) - 1):
        if (nums[i] >= nums[i - 1] and nums[i] <= nums[i + 1]) or (nums[i] <= nums[i - 1] and nums[i] >= nums[i + 1]): count = 0
        else: return False
    return True
#4.
#5.
#6.
#7.
#8.
#9.
#10.