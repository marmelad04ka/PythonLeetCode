#1. https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/description/
from typing import List


def minElement(self, nums: List[int]) -> int:
    min_n = 0
    for i in nums:
        num = (sum(map(int, str(i))))
        if min_n == 0:
            min_n = num
        elif min_n > num:
            min_n = num
    return min_n

#2. https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/description/
def maxProduct(self, nums: List[int]) -> int:
    len_nums = len(nums)
    nums.sort()
    return (nums[len_nums - 1] - 1) * (nums[len_nums - 2] - 1)

#3. https://leetcode.com/problems/find-closest-person/description/
def findClosest(self, x: int, y: int, z: int) -> int:
    if abs(z - x) == abs(z - y):
        return 0
    elif abs(z - x) > abs(z - y):
        return 2
    else:
        return 1

#4. https://leetcode.com/problems/find-the-integer-added-to-array-i/description/
def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
    min_nums1 = min(nums1)
    min_nums2 = min(nums2)

    if min_nums1 < min_nums2 or min_nums1 > min_nums2:
        return min_nums2 - min_nums1
    else:
        return 0

#5. https://leetcode.com/problems/kth-distinct-string-in-an-array/description/
def kthDistinct(self, arr: List[str], k: int) -> str:
    count, result = 0, 0
    for i in arr:
        if arr.count(i) == 1:
            count += 1
            if count == k:
                return i
    return ""

#6. https://leetcode.com/problems/check-balanced-string/description/
def isBalanced(self, num: str) -> bool:
    even, odd = 0, 0
    for index, char in enumerate(num):
        if index % 2 == 0:
            even += int(char)
        else: odd += int(char)
    return even == odd

#7. https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing/description/
def minOperations(self, nums: List[int]) -> int:
    result = 0
    for index, char in enumerate(nums[1:]):
        if nums[index + 1] <= nums[index]:
            result += nums[index] - nums[index + 1] + 1
            nums[index + 1] +=  nums[index] - nums[index + 1] + 1
    return result

#8. https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index/description/
def smallestIndex(self, nums: List[int]) -> int:
    sum_of_digits = 0
    for index, char in enumerate(nums):
        for digit in str(char):
            sum_of_digits += int(digit)
        if sum_of_digits == index: return index
        sum_of_digits = 0
    return -1

#9. https://leetcode.com/problems/third-maximum-number/description/
def thirdMax(self, nums: List[int]) -> int:
    array = sorted(set(nums), reverse = True)
    return array[2] if len(array) >= 3 else max(array)

#10.