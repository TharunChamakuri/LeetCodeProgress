class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        seen = set()
        a , b = -1 , -1
        maximum , minimum = -1 , float("inf")
        for num in grid:
            for n in num:
                if n in seen:
                    a = n
                else:
                    seen.add(n)
                minimum = min(n , minimum)
                maximum = max(n , maximum)
        for i in range(minimum , maximum + 1):
            if i not in seen:
                b = i
        if b == -1:
            if 1 not in seen:
                b = 1
            else:
                b = maximum + 1
        return [a , b]

        