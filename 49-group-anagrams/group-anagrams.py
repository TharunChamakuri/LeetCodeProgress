class Solution(object):
    def groupAnagrams(self, strs):
        HashMap = {}
        for ch in strs:
            word = "".join(sorted(ch))
            if word not in HashMap:
                HashMap[word] = []
            HashMap[word].append(ch)
        return list(HashMap.values())