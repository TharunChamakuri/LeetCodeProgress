class Solution(object):
    def lengthOfLongestSubstring(self, s):
        HashSet = set()
        res = 0
        l = 0
        for r in range(len(s)):
            while s[r] in HashSet:
                HashSet.remove(s[l])
                l += 1
            HashSet.add(s[r])
            res = max(res , (r - l + 1))
        return res