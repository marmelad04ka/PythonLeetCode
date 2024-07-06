from typing import List
#1. https://leetcode.com/problems/count-pairs-of-similar-strings/description/
def similarPairs(self, words: List[str]) -> int:
    n1 = [sorted(''.join(set(i))) for i in words]
    res = 0
    for i in range(len(n1)):
        for j in range(i + 1, len(n1)):
            if n1[i] == n1[j]: res += 1
    return res

#2. https://leetcode.com/problems/greatest-english-letter-in-upper-and-lower-case/description/
def greatestLetter(self, s: str) -> str:
    s1 = list(set(s))
    res = []
    for i in s1:
        if i.lower() in s and i.upper() in s: res += i.upper()
    if len(res) == 0: return ""
    return sorted(res)[::-1][0]

#3. https://leetcode.com/problems/time-needed-to-buy-tickets/description/
def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
    sumT = 0
    while True:
        for i in range(len(tickets)):
            if tickets[k] == 0: break
            if tickets[i] == 0: continue
            tickets[i] -= 1
            sumT += 1
        if tickets[k] == 0: break
    return sumT

#4. https://leetcode.com/problems/find-the-array-concatenation-value/description/
def findTheArrayConcVal(self, nums: List[int]) -> int:
    sumAll = 0
    for i in range(int(len(nums)/2)):
        sumAll += int(str(nums[i]) + str(nums[len(nums)-(i+1)]))
    if len(nums)%2 != 0: sumAll += nums[int(len(nums)/2)]
    return sumAll

#5.
#6.
#7.
#8.
#9.
#10.