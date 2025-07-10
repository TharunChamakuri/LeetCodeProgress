class Solution(object):
    def searchRange(self, nums, target):
        res = []
        for i in range(len(nums)):
            if target == nums[i]:
                res.append(i)
        if len(res) > 1:
            return [res[0],res[-1]]
        elif len(res) == 1:
            return [res[0] , res[0]]
        elif len(res) == 0:
            return [-1,-1]
        