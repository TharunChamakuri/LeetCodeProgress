class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows , cols = len(grid) , len(grid[0])
        res = [[float("inf")] * (cols + 1) for _ in range(rows + 1)]
        res[rows - 1][cols] = 0
        for r in range(rows - 1,-1,-1):
            for c in range(cols - 1,-1,-1):
                res[r][c] = grid[r][c] + min(res[r + 1][c] , res[r][c + 1])
        return res[0][0]