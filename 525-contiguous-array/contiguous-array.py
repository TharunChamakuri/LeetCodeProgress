class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        diff = {}
        res , zero , one = 0 , 0 , 0
        for i , n in enumerate(nums):
            if n == 0:
                zero += 1
            else:
                one += 1
            if one - zero not in diff:
                diff[one - zero] = i
            if zero == one:
                res = zero + one
            else:
                idx = diff[one - zero]
                res = max(res , i - idx)
        return res