#1. https://leetcode.com/problems/find-the-number-of-good-pairs-i/description/
def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
    res = 0
    for i in nums1:
        for j in nums2:
            if i < j: continue
            if i % (j * k) == 0:
                res += 1
    return res

#2. https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/description/
def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
    arr = []
    sumN = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[j] < nums[i]:
                sumN += 1
        arr.append(sumN)
        sumN = 0
    return arr

#3. https://leetcode.com/problems/running-sum-of-1d-array/description/
def runningSum(self, nums: List[int]) -> List[int]:
    arr1 = []
    l1 = len(nums)
    for i in range(l1 - 1):
        arr1.append(sum(nums[:-l1 + 1 + i]))
    arr1.append(sum(nums))
    return arr1

#4. https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/description/
def subtractProductAndSum(self, n: int) -> int:
    sumD = 0
    pD = 1
    l1 = []
    while n > 0:
        l1.append(n % 10)
        n = n // 10
    for i in range(len(l1)):
        sumD += l1[i]
        pD *= l1[i]
    return pD - sumD

#5. https://leetcode.com/problems/sum-of-values-at-indices-with-k-set-bits/description/
def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
    res = 0
    for i in range(len(nums)):
        if str(bin(i)[2:]).count('1') == k:
            res += nums[i]
    return res

#6. https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/description/
def mostWordsFound(self, sentences: List[str]) -> int:
    res = 0
    for i in range(len(sentences)):
        l1 = sentences[i].split(" ")
        if len(l1) > res:
            res = len(l1)
    return res

#7. https://leetcode.com/problems/left-and-right-sum-differences/description/
def leftRightDifference(self, nums: List[int]) -> List[int]:
    arr1 = []
    leftArr = []
    testArr= []
    for i in range(len(nums)):
        leftArr.append(sum(nums[:-len(nums) + i]))
        testArr.append(sum(nums[i + 1:]))
    for i in range(len(leftArr)):
        arr1.append(abs(leftArr[i] - testArr[i]))
    return arr1

#8. https://leetcode.com/problems/reverse-prefix-of-word/description/
def reversePrefix(self, word: str, ch: str) -> str:
    if word.count(ch) == 0: return word
    ind = word.index(ch)
    l1 = list(word[:ind + 1])
    l1.reverse()
    end = word[ind + 1:]
    return ''.join(l1) + end

#9. https://leetcode.com/problems/create-target-array-in-the-given-order/description/
def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
    arr = []
    for i in range(len(nums)):
        arr.insert(index[i], nums[i])
    return arr

#10. https://leetcode.com/problems/decompress-run-length-encoded-list/
def decompressRLElist(self, nums: List[int]) -> List[int]:
    arr = []
    for i in range(1, len(nums), 2):
        arr += [nums[i]] * nums[i - 1]
    return arr