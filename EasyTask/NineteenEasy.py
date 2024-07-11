from typing import List
#1. https://leetcode.com/problems/count-integers-with-even-digit-sum/description/
def sumOfDigit(n):
    strr = str(n)
    list_of_number = list(map(int, strr.strip()))
    return sum(list_of_number)
def countEven(self, num: int) -> int:
    count = 0
    for i in range(num - num%10, num + 1):
        if sumOfDigit(i)%2 == 0: count += 1
    return (num//10) * 5 - 1 + count

#2. https://leetcode.com/problems/add-digits/description/
def sum_of_digits(number):
    sum_digits = 0
    while number > 0:
        sum_digits += number % 10
        number //= 10
    return sum_digits
def addDigits(self, num: int) -> int:
    while True:
        if num < 10: break
        num = sum_of_digits(num)
    return num

#3. https://leetcode.com/problems/take-gifts-from-the-richest-pile/description/
def pickGifts(self, gifts: List[int], k: int) -> int:
    for i in range(1, k + 1):
        gifts.sort()
        gifts[len(gifts) - 1] = int(gifts[len(gifts) - 1] ** 0.5)
    return sum(gifts)

#4. https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/description/
def divideString(self, s: str, k: int, fill: str) -> List[str]:
    result = []
    lenS = len(s)
    for i in range(lenS, lenS + k):
        if i%k == 0: s += fill * (i - lenS)
    for i in range(0, lenS, k):
        result.append(s[i: i + k])
    return result

#5.
#6.
#7.
#8.
#9.
#10.