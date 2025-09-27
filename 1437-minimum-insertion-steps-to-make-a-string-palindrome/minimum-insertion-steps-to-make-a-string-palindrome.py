class Solution:
    def minInsertions(self, s: str) -> int:
        rev = s[::-1]
        m = len(s)
        dp = [[0]* (m+1) for _ in range(m+1)]

        for i in range(m-1 , -1 , -1):
            for j in range(m-1 , -1 , -1):
                if s[i] == rev[j]:
                    dp[i][j] = dp[i+1][j+1] + 1
                else:
                    dp[i][j] = max(dp[i+1][j] , dp[i][j+1])
        return (m - dp[0][0])