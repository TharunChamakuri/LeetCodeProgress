class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        freq = {}
        for w in words:
            freq[w] = freq.get(w , 0) + 1
        res = []
        wordlen = len(words[0])
        windowlen = len(words) * wordlen
        for i in range(len(s) - windowlen + 1):
            j = i
            subfreq = {}
            while j < i + windowlen:
                substr = s[j : j + wordlen]
                if substr not in freq:
                    break
                subfreq[substr] = subfreq.get(substr , 0) + 1
                if subfreq[substr] > freq[substr]:
                    break
                j += wordlen
            if  j == i + windowlen:
                res.append(i)
        return res