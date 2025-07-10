class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        while len(s) % k != 0:
            s += fill
        l = 0
        r = 0
        res = []
        while l < len(s) and r < len(s):
            r = l + k
            res.append(s[l:r])
            l = r
        return res

            