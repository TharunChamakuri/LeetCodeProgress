class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        CountMap = {}
        for c in nums:
            CountMap[c] = CountMap.get(c , 0) + 1
        count = 0
        n = len(nums) // 2
        for key in CountMap:
            if CountMap[key] % 2 == 0:
                count += CountMap[key] // 2
        if count == n:
            return True
        else:
            return False