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

#4. https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/
def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
    setNums = set(nums)
    res = []
    for i in range(1, len(nums) + 1):
        if i not in setNums:
            res.append(i)
    return res

#5. https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/description/
def findSpecialInteger(self, arr: List[int]) -> int:
    bigChe = len(arr) * 0.25
    count = 1
    for i in range(len(arr) - 1):
        if arr[i] == arr[i + 1]:
            count += 1
        else:
            if count > bigChe: return arr[i]
            count = 1
    return arr[-1]

#6. https://leetcode.com/problems/complement-of-base-10-integer/description/
def bitwiseComplement(self, n: int) -> int:
    binNRepl = ''
    for i in bin(n)[2:]:
        if i == '1': binNRepl += '0'
        else: binNRepl += '1'
    return int(binNRepl, 2)

#7. https://leetcode.com/problems/best-poker-hand/description/
def bestHand(self, ranks: List[int], suits: List[str]) -> str:
    dirCard = {}
    if len(set(suits)) == 1: return 'Flush'
    for i in ranks:
        if i in dirCard: dirCard[i] += 1
        else: dirCard[i] = 1
    max_key = max(dirCard, key=dirCard.get)
    if dirCard.get(max_key) >= 3: return 'Three of a Kind'
    if dirCard.get(max_key) == 2: return 'Pair'
    return 'High Card'

#8. https://leetcode.com/problems/average-value-of-even-numbers-that-are-divisible-by-three/description/
def averageValue(self, nums: List[int]) -> int:
    allN, sumN = 0, 0
    for i in tuple(nums):
        if i%3 == 0 and i%2 == 0:
            sumN += i
            allN += 1
    return 0 if allN == 0 else int(sumN/allN)

#9. https://leetcode.com/problems/kth-missing-positive-number/description/
def findKthPositive(self, arr: List[int], k: int) -> int:
    count = 0
    for i in range(1, arr[-1] + 1):
        if i not in arr:
            count += 1
        if count == k: return i
    return arr[-1] + k - count

#10. https://leetcode.com/problems/consecutive-characters/description/
def maxPower(self, s: str) -> int:
    arr = []
    count = 1
    for i in range(len(s)):
        if i == len(s) - 1:
            arr.append(count)
            break
        if s[i] == s[i + 1]: count += 1
        else:
            arr.append(count)
            count = 1
    return max(arr)