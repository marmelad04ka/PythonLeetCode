#58. https://leetcode.com/problems/length-of-last-word/description/
def lengthOfLastWord(self, s: str) -> int:
    return len(s.split()[-1])

#67. https://leetcode.com/problems/add-binary/description/
def addBinary(self, a: str, b: str) -> str:
    return bin(int(a, 2) + int(b, 2))[2:]

#70. https://leetcode.com/problems/climbing-stairs/description/
def climbStairs(self, n: int) -> int:
    first, second = 1, 2
    if n <= 2: return n
    for i in range(n - 2):
        second += first
        first = second - first
    return second
#1.
#1.
#1.
#1.
#1.
#1.
#1.