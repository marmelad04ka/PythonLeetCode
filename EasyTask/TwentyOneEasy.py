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

#6. https://leetcode.com/problems/string-matching-in-an-array/description/
def stringMatching(self, words: List[str]) -> List[str]:
    sorted_words = sorted(words, key=lambda x: len(x))
    result = []
    for i in range(len(sorted_words)):
        for ii in range(i+1, len(sorted_words)):
            if sorted_words[i] in sorted_words[ii] and sorted_words[i] not in result:
                result.append(sorted_words[i])
    return result

#7. https://leetcode.com/problems/check-whether-two-strings-are-almost-equivalent/description/
def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
    uniq_w1 = set(word1 + word2)
    for i in uniq_w1:
        if abs(word1.count(i) - word2.count(i)) >= 4: return False
    return True

#8. https://leetcode.com/problems/valid-perfect-square/description/
def isPerfectSquare(self, num: int) -> bool:
    return (num ** 0.5).is_integer()

#9. https://leetcode.com/problems/longest-common-prefix/description/
def longestCommonPrefix(self, strs: List[str]) -> str:
    if len(strs) == 1: return ''.join(strs)
    strs = sorted(strs, key=lambda x: len(x))
    mid = ''
    result = ''
    for i in range(len(strs[0])):
        for ii in strs:
            mid += ii[i]
        if mid.replace(mid[0], "") == "":
            result += mid[0]
        else: return result
        mid = ""
    return result

#10. https://leetcode.com/problems/occurrences-after-bigram/description/
def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
    l1 = text.split(" ")
    result = []
    for i in range(len(l1) - 2):
        if l1[i] == first and l1[i + 1] == second:
            result.append(l1[i + 2])
    return result