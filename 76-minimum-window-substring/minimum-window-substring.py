class Solution(object):
    def minWindow(self, s, t):
        if not t:
            return ""
        freq = {}
        temp = {}
        for ch in t:
            freq[ch] = freq.get(ch , 0) + 1
        have , need = 0 , len(freq)
        resLen , res , l = len(s) + 1 , [] , 0
        for r in range(len(s)):
            ch = s[r]
            if ch in freq:
                temp[ch] = temp.get(ch , 0) + 1
                if temp[ch] == freq[ch]:
                    have += 1
            while have == need:
                if (r - l + 1) < resLen and r < len(s):
                    res = s[l:r + 1]
                    resLen = r - l + 1
                if s[l] in temp:
                    temp[s[l]] -= 1
                    if temp[s[l]] < freq[s[l]]:
                        have -= 1
                l += 1
        return res if resLen != len(s) + 1 else ""