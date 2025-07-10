class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l , r = 0 , 0
        while l < len(haystack):
            if haystack[l] == needle[r]:
                l , r = l + 1, r + 1
                if r == len(needle):
                    return abs(l - r)
            elif r > 0:
                l = abs(r - l) + 1
                r = 0
            else:
                l += 1
        return -1