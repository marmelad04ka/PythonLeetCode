from typing import List
#1. https://leetcode.com/problems/reverse-only-letters/description/
def reverseOnlyLetters(self, s: str) -> str:
    reverseS = [s[i] for i in range(len(s) - 1, -1, -1) if s[i].isalpha()]
    for i in range(len(s)):
        if not s[i].isalpha():
            reverseS.insert(i, s[i])
    return ''.join(reverseS)

#2. https://leetcode.com/problems/valid-anagram/description/
def isAnagram(self, s: str, t: str) -> bool:
    return sorted(s) == sorted(t)

#3. https://leetcode.com/problems/furthest-point-from-origin/description/
def furthestDistanceFromOrigin(self, moves: str) -> int:
    count = 0
    cR = moves.count('R')
    cL = moves.count('L')
    if cR == cL or cL > cR: moves = moves.replace('_', 'L')
    if cR > cL: moves = moves.replace('_', 'R')
    for i in moves:
        if i == 'L': count -= 1
        else: count += 1
    return abs(count)

#4. https://leetcode.com/problems/capitalize-the-title/description/
def capitalizeTitle(self, title: str) -> str:
    res = ''
    for i in title.lower().split(" "):
        if len(i) > 2: res += i.title() + " "
        else: res += i + " "
    return res.strip()

#5. https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/description/
def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
    res = ''
    lenS = len(searchWord)
    l1 = sentence.split(" ")
    for i in range(len(l1)):
        if len(l1[i]) < lenS: continue
        if l1[i][:lenS] == searchWord: return i + 1
    return -1
#6.
#7.
#8.
#9.
#10.