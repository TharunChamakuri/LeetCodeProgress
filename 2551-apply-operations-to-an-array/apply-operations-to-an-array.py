class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(1,len(nums)):
            if nums[i] == nums[i - 1]:
                nums[i - 1] = nums[i - 1] * 2
                nums[i] = 0
            res.append(0)
        res.append(0)
        k = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                res[k] = nums[i]
                k += 1
        return res
        