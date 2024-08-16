from typing import List
#1. https://leetcode.com/problems/find-the-k-beauty-of-a-number/description/
def divisorSubstrings(self, num: int, k: int) -> int:
    sN = str(num)
    count = 0
    for i in range(len(sN)):
        if len(sN[i:i + k]) < k: break
        if int(sN[i:i + k]) != 0:
            if num % int(sN[i:i + k]) == 0: count += 1
        else:
            continue
    return count

#2. https://leetcode.com/problems/max-consecutive-ones/description/
def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    arr = []
    count = 0
    for i in nums:
        if i == 1: count += 1
        else:
            arr.append(count)
            count = 0
    arr.append(count)
    return max(arr)

#3. https://leetcode.com/problems/find-the-difference/description/
def findTheDifference(self, s: str, t: str) -> str:
    s = sorted(s)
    t = sorted(t)
    for i in range(len(t)):
        if i == len(t) - 1 or t[i] != s[i]: return t[i]

#4. https://leetcode.com/problems/count-elements-with-strictly-smaller-and-greater-elements/description/
def countElements(self, nums: List[int]) -> int:
    maxN, minN, count = max(nums), min(nums), 0
    for i in nums:
        if i != minN and i != maxN: count += 1
    return count

#5. https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/description/
def minimumOperations(self, nums: List[int]) -> int:
    return sum([1 for i in nums if i%3 != 0])

#6. https://leetcode.com/problems/odd-string-difference/description/
def oddString(self, words: List[str]) -> str:
    arr = [[],[],[]]
    mid = []
    for j in range(3):
        for i in range(1, len(words[j])):
            arr[j].append(ord(words[j][i]) - ord(words[j][i - 1]))
    if arr[0] != arr[1] and arr[0] != arr[2]: return words[0]
    elif arr[0] != arr[1] and arr[0] == arr[2]: return words[1]
    elif arr[0] == arr[1] and arr[0] != arr[2]: return words[2]
    else:
        for i in range(3, len(words)):
            for j in range(1, len(words[i])):
                mid.append(ord(words[i][j]) - ord(words[i][j - 1]))
            if arr[0] != mid: return words[i]
            mid = []
    return ''

#7. https://leetcode.com/problems/slowest-key/description/
def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
    arr = []
    res = ''
    for i in range(len(releaseTimes)):
        if i == 0: arr.append(releaseTimes[i])
        else: arr.append(releaseTimes[i] - releaseTimes[i - 1])
    maxArr = max(arr)
    for i in range(len(arr)):
        if arr[i] == maxArr: res += keysPressed[i]
    return max(res)

#8. https://leetcode.com/problems/rotate-string/description/
def rotateString(self, s: str, goal: str) -> bool:
    for i in range(len(s)):
        if s[i:] + s[:i] == goal: return True
    return False

#9. https://leetcode.com/problems/minimum-common-value/description/
def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
    arr = list(set(nums1)) + list(set(nums2))
    arr.sort()
    for i in range(len(arr) - 1):
        if arr[i] == arr[i + 1]: return arr[i]
    return -1

#10. https://leetcode.com/problems/intersection-of-two-arrays-ii/description/
def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    arr = set(nums1)
    result = []
    for i in arr:
        if i in nums2:
            result += [i] * min(nums1.count(i), nums2.count(i))
    return result