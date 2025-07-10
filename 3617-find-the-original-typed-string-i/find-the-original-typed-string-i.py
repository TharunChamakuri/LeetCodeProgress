class Solution:
    def possibleStringCount(self, word: str) -> int:
        count = 1
        for i in range(len(word)):
            if i + 1 < len(word) and word[i] == word[i + 1]:
                count += 1
        return count