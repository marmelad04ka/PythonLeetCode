from typing import List
#1. https://leetcode.com/problems/squares-of-a-sorted-array/description/
def sortedSquares(self, nums: List[int]) -> List[int]:
    return sorted([i * i for i in nums])

#2. https://leetcode.com/problems/count-prefixes-of-a-given-string/description/
def countPrefixes(self, words: List[str], s: str) -> int:
    result = 0
    for i in words:
        if i in s[:len(i)]:
            result += 1
    return result

#3. https://leetcode.com/problems/fizz-buzz/description/
def fizzBuzz(self, n: int) -> List[str]:
    res = []
    for i in range(1, n + 1):
        if i%3 == 0 and i%5 == 0: res.append('FizzBuzz')
        elif i%5 == 0: res.append("Buzz")
        elif i%3 == 0: res.append('Fizz')
        else: res.append(str(i))
    return res

#4.
#5.
#6.
#7.
#8.
#9.
#10.