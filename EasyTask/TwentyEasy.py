from typing import List
#1. https://leetcode.com/problems/existence-of-a-substring-in-a-string-and-its-reverse/description/
def isSubstringPresent(self, s: str) -> bool:
    reS = s[::-1]
    for i in range(len(s) - 1):
        timeStr = s[i] + s[i + 1]
        if timeStr in reS: return True
        timeStr = ''
    return False

#2. https://leetcode.com/problems/defuse-the-bomb/description/
def decrypt(self, code: List[int], k: int) -> List[int]:
    result = []
    if k > -1:
        for i in range(len(code)):
            if i + k > len(code) - 1: result.append(sum(code[i+1:] + code[:k - len(code[i+1:])]))
            else: result.append(sum(code[i+1:k+1+i]))
    else:
        for i in range(len(code)):
            if i + k < 0: result.append(sum(code[len(code) + i + k:] + code[:-k - len(code[len(code) + i + k:])]))
            else: result.append(sum(code[i + k:-k + (i + k)]))
    return result

#3. https://leetcode.com/problems/reformat-phone-number/description/
def reformatNumber(self, number: str) -> str:
    newNumber = number.replace('-', '').replace(" ", "")
    result = []
    count = 0
    while True:
        for i in range(len(newNumber)):
            if len(newNumber) == 2:
                result.append(newNumber[i] + newNumber[i + 1])
                newNumber = newNumber[i + 2:]
                break
            if len(newNumber) == 4:
                result.append(newNumber[i] + newNumber[i + 1])
                result.append(newNumber[i + 2] + newNumber[i + 3])
                newNumber = newNumber[i + 4:]
                break
            if len(newNumber) > 2:
                result.append(newNumber[i] + newNumber[i + 1] + newNumber[i + 2])
                newNumber = newNumber[i + 3:]
                break
        if len(newNumber) == 0: break
    return '-'.join(result)

#4. https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/description/
def minStartValue(self, nums: List[int]) -> int:
    if min(nums) > 0: return 1
    minN = 1
    count = 0
    while True:
        count = minN
        for i in range(len(nums)):
            count += nums[i]
            if count < 1:
                minN += 1
                break
        if count > 0: return minN

#5. https://leetcode.com/problems/last-stone-weight/description/
def lastStoneWeight(self, nums: List[int]) -> int:
    nums.sort()
    nums.reverse()
    while True:
        for i in range(len(nums)):
            if len(nums) == 1 or len(nums) == 0: break
            if nums[i] - nums[i + 1] != 0:
                nums.append(nums[i] - nums[i + 1])
                nums.pop(i)
                nums.pop(i)
                break
            if nums[i] - nums[i + 1] == 0:
                nums.pop(i)
                nums.pop(i)
                break
        nums.sort()
        nums.reverse()
        if len(nums) == 1: return nums[0]
        if len(nums) == 0: return 0

#6. https://leetcode.com/problems/sign-of-the-product-of-an-array/description/
def arraySign(self, nums: List[int]) -> int:
    if nums.count(0) > 0: return 0
    elif len([i for i in nums if i < 1])%2 == 0: return 1
    else: return -1

#7. https://leetcode.com/problems/minimum-number-of-operations-to-convert-time/description/
def convertTime(self, current: str, correct: str) -> int:
    count = 0
    minute = 0
    if current[3:] > correct[3:]:
        count += int(correct[:2]) - int(current[:2]) - 1
        minute = int(correct[:2]) * 60 + int(correct[3:]) - (int(current[:2]) * 60 + int(current[3:])) - count * 60
    else:
        count += int(correct[:2]) - int(current[:2])
        minute = int(correct[3:]) - int(current[3:])
    count += minute//15
    minute -= (minute//15) * 15
    count += minute//5
    minute -= (minute//5) * 5
    count += minute
    return count
#8. https://leetcode.com/problems/count-the-number-of-special-characters-i/description/
def numberOfSpecialChars(self, word: str) -> int:
    count = 0
    uniq = set(word.lower())
    for i in uniq:
        if i in word and i.upper() in word: count += 1
    return count

#9. https://leetcode.com/problems/count-prefix-and-suffix-pairs-i/description/
def countPrefixSuffixPairs(self, words: List[str]) -> int:
    count = 0
    for i in range(len(words)):
        for ii in range(i+ 1, len(words), 1):
            if words[i] == (words[ii][:len(words[i])]) and (words[i] == words[ii][len(words[ii]) - len(words[i]):]): count += 1
    return count

#10. https://leetcode.com/problems/majority-element/description/
def majorityElement(self, nums: List[int]) -> int:
    l1 = set(nums)
    for i in l1:
        if nums.count(i) > (len(nums)/2): return i