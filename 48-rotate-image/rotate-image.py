class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        m = len(matrix)
        n = len(matrix[0])
        res = []
        for r in range(m):
            arr = []
            for c in range(n):
                arr.append(matrix[c][r])
            arr.reverse()
            res.append(arr)
        for num in range(m):
            matrix[num] = res[num]
        