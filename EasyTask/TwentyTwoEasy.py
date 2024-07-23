from typing import List
#1. https://leetcode.com/problems/largest-odd-number-in-string/description/
def largestOddNumber(self, num: str) -> str:
    l1 = num[::-1]
    res = ''
    for i in range(len(l1)):
        if int(l1[i]) % 2 != 0:
            res += l1[i:]
            break
    return res[::-1]

#2. https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/description/
def average(self, salary: List[int]) -> float:
    salary.sort()
    return sum(salary[1:len(salary) - 1])/len(salary[1:len(salary) - 1])

#3. https://leetcode.com/problems/valid-parentheses/description/
def isValid(self, s: str) -> bool:
    if len(s)%2 != 0: return False
    res = ''
    for i in s:
        if i in '({[': res += i
        elif len(res) != 0 and ((i == ')' and res[-1] == '(') or (i == ']' and res[-1] == '[') or (i == '}' and res[-1] == '{')): res = res[:-1]
        else: return False
    return res == ''
#4.
#5.
#6.
#7.
#8.
#9.
#10.