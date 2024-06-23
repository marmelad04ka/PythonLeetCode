from typing import List
#1. https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/description/
def finalPrices(self, prices: List[int]) -> List[int]:
    res = []
    mid = 0
    for i in range(len(prices)):
        if i > len(prices) - 2:
            res.append(prices[i])
            continue
        if prices[i] > prices[i + 1]:
            res.append(prices[i] - prices[i + 1])
        else:
            for ii in range(i + 1, len(prices)):
                if prices[ii] <= prices[i]:
                    mid = prices[ii]
                    break
            res.append(prices[i] - mid)
            mid = 0
    return res

#2. https://leetcode.com/problems/find-greatest-common-divisor-of-array/description/
def findGCD(self, nums: List[int]) -> int:
    larg = max(nums)
    small = min(nums)
    res = 0
    for i in range(small, 0, -1):
        if small%i == 0 and larg%i == 0:
            res = i
            break
    return res
#3.
#4.
#5.
#6.
#7.
#8.
#9.
#10.
