from typing import List
#1. https://leetcode.com/problems/distribute-candies/description/
def distributeCandies(self, candyType: List[int]) -> int:
    return len(sorted(set(candyType))[:int(len(candyType) / 2)])

#2. https://leetcode.com/problems/count-square-sum-triples/description/
def countTriples(self, n: int) -> int:
    result = 0
    sqrtN = [i * i for i in range(1, n + 1)]
    for i in range(len(sqrtN)):
        for j in range(len(sqrtN)-1, i, -1):
            if sqrtN[i] + sqrtN[j] in sqrtN: result += 2
    return result

#3. https://leetcode.com/problems/number-complement/description/
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

#4.
#5.
#6.
#7.
#8.
#9.
#10.
