class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        for l in range(len(s)-1,-1,-1):
            for w in wordDict:
                if l + len(w) <= len(s) and s[l:len(w) + l] == w:
                    dp[l] = dp[l + len(w)]
                if dp[l]:
                    break
        return dp[0]