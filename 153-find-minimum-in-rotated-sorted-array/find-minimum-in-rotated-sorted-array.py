class Solution(object):
    def findMin(self, nums):
        if not nums:
            return None
        Min = nums[0]
        for i in range(len(nums)):
            if Min > nums[i]:
                Min = nums[i]
        return Min