class Solution(object):
    def maximumSum(self, nums):
        HashMap = {}
        res = -1
        for n in nums:
            str1 = str(n)
            Sum = 0
            for s in str1:
                Sum += int(s)
            if Sum in HashMap:
                HashMap[Sum].append(n)
            else:
                HashMap[Sum] = [n]
        for key in HashMap:
            if len(HashMap[key]) > 1:
                HashMap[key].sort(reverse=True)
                res = max(res, HashMap[key][0] + HashMap[key][1])
        return res