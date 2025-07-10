class Solution(object):
    def wordPattern(self, pattern, s):
        string = s.split(" ")
        if len(pattern) != len(string):
            return False
        mapPS , mapSP = {} , {}
        for c1,c2 in zip(pattern,string):
            if((c1 in mapPS and mapPS[c1] != c2) or
                (c2 in mapSP and mapSP[c2] != c1)):
                return False
            mapPS[c1] = c2
            mapSP[c2] = c1
        return True