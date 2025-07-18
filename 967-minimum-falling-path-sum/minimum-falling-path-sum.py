class Solution(object):
    def minFallingPathSum(self, matrix):
        n = len(matrix)
        for r in range(1,n):
            for c in range(n):
                mid = matrix[r-1][c]
                left = matrix[r-1][c-1] if c - 1 >= 0 else float("inf")
                right = matrix[r-1][c+1] if c+1 < n else float("inf")
                matrix[r][c] += min(mid , left , right)
        return min(matrix[-1])