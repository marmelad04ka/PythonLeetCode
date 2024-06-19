from typing import List
#1. https://leetcode.com/problems/jewels-and-stones/description/
def numJewelsInStones(self, jewels: str, stones: str) -> int:
    res = 0
    for i in jewels:
        res += stones.count(i)
    return res

#2. https://leetcode.com/problems/shuffle-the-array/description/
def shuffle(self, nums: List[int], n: int) -> List[int]:
    arr1 = []
    for i in range(len(nums)):
        if i == n: break
        arr1.append(nums[i])
        arr1.append(nums[i + n])
    return arr1

#3. https://leetcode.com/problems/find-words-containing-character/description/
def findWordsContaining(self, words: List[str], x: str) -> List[int]:
    arr = []
    for i in range(len(words)):
        if words[i].count(x) > 0:
            arr.append(i)
    return arr

#4. https://leetcode.com/problems/richest-customer-wealth/description/
def maximumWealth(self, accounts: List[List[int]]) -> int:
    res = 0
    mid = 0
    for i in range(len(accounts)):
        mid = sum(accounts[i])
        if mid > res:
            res = mid
    return res

#5. https://leetcode.com/problems/add-two-integers/description/
def sum(self, num1: int, num2: int) -> int:
    return num1 + num2

#6. https://leetcode.com/problems/smallest-even-multiple/description/
def smallestEvenMultiple(self, n: int) -> int:
    i = 1
    while i != -1:
        if n*i%2 == 0:
            return n * i
        i += 1

#7. https://leetcode.com/problems/number-of-employees-who-met-the-target/description/
def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
    res = 0
    for i in range(len(hours)):
        if hours[i] >= target:
            res += 1
    return res

#8. https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/
def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
    res = []
    maxN = max(candies)
    for i in range(len(candies)):
        if candies[i] + extraCandies >= maxN:
            res.append(True)
        else: res.append(False)
    return res

#9. https://leetcode.com/problems/goal-parser-interpretation/description/
def interpret(self, command: str) -> str:
    return command.replace('()', 'o').replace('(', "").replace(')', "")

#10. https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/description/
def countPairs(self, nums: List[int], target: int) -> int:
    res = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i < j and nums[i] + nums[j] < target:
                res += 1
    return res