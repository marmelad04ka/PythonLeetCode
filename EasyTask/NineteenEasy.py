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

#5. https://leetcode.com/problems/apple-redistribution-into-boxes/description/
def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
    capacity.sort()
    sumA = sum(apple)
    count = 1
    for i in range(len(capacity)-1, -1, -1):
        if sumA - capacity[i] > 0:
            sumA -= capacity[i]
            count += 1
        else: break
    return count

#6. https://leetcode.com/problems/reformat-date/description/
def reformatDate(self, date: str) -> str:
    month = ['0',"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    l1 = date.split(" ")
    result = ''
    result += l1[2] + '-'
    if month.index(l1[1]) < 10: result += '0'
    result += str(month.index(l1[1])) + '-'
    if len(l1[0]) == 3: result += '0' + l1[0][:1]
    else: result += l1[0][:2]
    return result

#7. https://leetcode.com/problems/two-furthest-houses-with-different-colors/description/
def maxDistance(self, colors: List[int]) -> int:
    l1 = list(set(colors))
    result = 0
    for i in range(len(l1)):
        for ii in range(len(colors) - 1, -1, -1):
            if colors[ii] != l1[i]:
                if ii - colors.index(l1[i]) > result: result = ii - colors.index(l1[i])
                break
    return result

#8. https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/description/
def divideString(self, s: str, k: int, fill: str) -> List[str]:
    result = []
    lenS = len(s)
    for i in range(lenS, lenS + k):
        if i%k == 0: s += fill * (i - lenS)
    for i in range(0, lenS, k):
        result.append(s[i: i + k])
    return result

#9. https://leetcode.com/problems/calculate-digit-sum-of-a-string/description/
def digitSum(self, s: str, k: int) -> str:
    res = ''
    while len(s) > k:
        for i in range(0, len(s), k):
            str1 = s[i: i + k]
            res += str(sum(int(digit) for digit in str1))
        s = res
        res = ""
    return s

#10. https://leetcode.com/problems/sort-colors/description/
def sortColors(self, nums: List[int]) -> None:
    nums.sort()