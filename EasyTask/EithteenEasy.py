from typing import List
from collections import Counter

#575. https://leetcode.com/problems/distribute-candies/description/
def distributeCandies(self, candyType: List[int]) -> int:
    return len(sorted(set(candyType))[:int(len(candyType) / 2)])

#1925. https://leetcode.com/problems/count-square-sum-triples/description/
def countTriples(self, n: int) -> int:
    result = 0
    sqrtN = [i * i for i in range(1, n + 1)]
    for i in range(len(sqrtN)):
        for j in range(len(sqrtN)-1, i, -1):
            if sqrtN[i] + sqrtN[j] in sqrtN: result += 2
    return result

#476. https://leetcode.com/problems/number-complement/description/
def binary_to_decimal(binary):
    decimal = 0
    power = len(binary) - 1
    for digit in binary:
        decimal += int(digit) * (2 ** power)
        power -= 1
    return decimal

def findComplement(self, num: int) -> int:
    numB = ''
    for i in str(bin(num)[2:]):
        if i == '1': numB += '0'
        else: numB += '1'
    return binary_to_decimal(numB)

#2460. https://leetcode.com/problems/apply-operations-to-an-array/description/
def applyOperations(self, nums: List[int]) -> List[int]:
    result = []
    for i in range(len(nums)):
        if i == len(nums) - 1:
            if nums[i] != 0: result.append(nums[i])
            break
        if nums[i] == nums[i + 1]:
            nums[i] += nums[i + 1]
            nums[i + 1] = 0
        if nums[i] != 0: result.append(nums[i])
    return result + [0] * nums.count(0)

#2639. https://leetcode.com/problems/find-the-width-of-columns-of-a-grid/description/
def findColumnWidth(self, matrix: List[List[int]]) -> List[int]:
    result = []
    lenS = 0
    for i in range(len(matrix)- (len(matrix) - len(matrix[0]))):
        for ii in range(len(matrix)):
            if lenS < len(str(matrix[ii][i])):
                lenS = len(str(matrix[ii][i]))
        result.append(lenS)
        lenS = 0
    return result

#1991. https://leetcode.com/problems/find-the-middle-index-in-array/description/
def findMiddleIndex(self, nums: List[int]) -> int:
    left_sum, total_sum = 0, sum(nums)
    for i, n in enumerate(nums):
        right_sum = total_sum - left_sum - n
        if left_sum == right_sum:
            return i
        left_sum += n
    return -1

#884. https://leetcode.com/problems/uncommon-words-from-two-sentences/description/
def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
    s3 = s1.split(" ") + s2.split(" ")
    unique = [val for val, cnt in Counter(s3).items() if cnt == 1]
    return unique

#268. https://leetcode.com/problems/missing-number/description/
def missingNumber(self, nums: List[int]) -> int:
    nums2 = [i for i in range(0, max(nums) + 1)]
    if sum(nums2) - sum(nums) == 0:
        if min(nums) == 0: return max(nums) + 1
        else: return 0
    return  sum(nums2) - sum(nums)

#1394. https://leetcode.com/problems/find-lucky-integer-in-an-array/description/
def findLucky(self, arr: List[int]) -> int:
    result = []
    arr1 = set(arr)
    for i in arr1:
        if i == arr.count(i): result.append(i)
    return max(result) if len(result) != 0 else -1

#929. https://leetcode.com/problems/unique-email-addresses/description/
def numUniqueEmails(self, emails: List[str]) -> int:
    numDog, numPlus = 0, 0
    result = []
    str1 = ''
    for i in emails:
        numDog = i.find("@")
        if '+' not in i: str1 += i[:numDog].replace('.', '')
        else:
            numPlus = i.find("+")
            str1 += i[:numPlus].replace('.', '')
        str1 += i[numDog:]
        if str1 not in result :result.append(str1)
        str1 = ""
    return len(result)