class Solution(object):
    def lengthOfLongestSubstring(self, s):
        HashMap = {}
        l = 0
        maxLen = 0
        for r in range(len(s)):
            while s[r] in HashMap:
                del HashMap[s[l]]
                l += 1
            HashMap[s[r]] = r
            maxLen = max(r - l + 1 , maxLen)
        return maxLen