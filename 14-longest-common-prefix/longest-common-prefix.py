class Solution(object):
    def longestCommonPrefix(self, strs):
        length = float("inf")
        for elem in strs:
            length = min(len(elem),length)
        elements = [['x'] * len(strs) for _ in range(length)]
        for r in range(len(strs)):
            for c in range(length):
                elements[c][r] = strs[r][c]
        res = ""
        for c in elements:
            if len(set(c)) == 1:
                res += c[0]
            else:
                break
        return res