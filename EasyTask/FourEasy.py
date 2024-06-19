#1. https://leetcode.com/problems/count-of-matches-in-tournament/description/
def numberOfMatches(self, n: int) -> int:
    k = 0
    n1 = n
    res = 0
    while k < n:
        mat = math.ceil((n1 - 1) / 2)
        if mat == 0: break
        team = n1 - mat
        n1 = team
        res += mat
        k += 1
    return res

#2. https://leetcode.com/problems/minimum-number-game/description/
def numberGame(self, nums: List[int]) -> List[int]:
    nums.sort()
    arr = []
    for i in range(1, len(nums), 2):
        arr.append(nums[i])
        arr.append(nums[i - 1])
    return arr

#3. https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-i/description/
def minOperations(self, nums: List[int], k: int) -> int:
    return sum([i * 0 + 1 for i in nums if i < k])

#4. https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/description/
def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
    w1 = ''.join(word1)
    w2 = ''.join(word2)
    return w1 == w2

#5. https://leetcode.com/problems/sum-multiples/description/
def sumOfMultiples(self, n: int) -> int:
    return sum([i for i in range(1, n + 1) if i%3 == 0 or i%5 == 0 or i%7 == 0])

#6. https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/description/
def numberOfSteps(self, num: int) -> int:
    obtain = 0
    res = 0
    for i in range(1, num + 1):
        if obtain == 1:
            res += 1
            break
        if num%2 == 0:
            obtain = num/2
        else:
            obtain = num - 1
        num = obtain
        res += 1
    return res

#7. https://leetcode.com/problems/truncate-sentence/description/
def truncateSentence(self, s: str, k: int) -> str:
    return " ".join(s.split(" ")[:k])

#8. https://leetcode.com/problems/shuffle-string/description/
def restoreString(self, s: str, indices: List[int]) -> str:
    arr = []
    for i in range(len(s)):
        arr.append(s[indices.index(i)])
    return ''.join(arr)

#9. https://leetcode.com/problems/count-the-digits-that-divide-a-number/description/
def countDigits(self, num: int) -> int:
    result = 0
    mid = num
    i = 0
    while i != num/2:
        if mid == 0: break
        if num%(mid%10) == 0:
            result += 1
        mid = mid//10
        i += 1
    return result

#10. https://leetcode.com/problems/decode-the-message/description/
def decodeMessage(self, key: str, message: str) -> str:
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    uniquel1 = list(dict.fromkeys(key.replace(" ", "")))
    result = ""
    for i in message:
        if i == " ":
            result += " "
            continue
        result += alphabet[uniquel1.index(i)]
    return result