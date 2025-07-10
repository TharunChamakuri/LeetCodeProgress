class Solution(object):
    def numSubseq(self, nums, target):
        nums.sort()
        mod = 10**9 + 7
        res = 0
        r = len(nums) - 1
        for l in range(len(nums)):
            while nums[l] + nums[r] > target and l <= r:
                r -= 1
            if l <= r:
                res += (2**(r - l))
                res %= mod
        return res
        