class Solution(object):
    def findLucky(self, arr):
        HashMap = {}
        res = -1
        for i , val in enumerate(arr):
            HashMap[val] = HashMap.get(val , 0) + 1
        for key in HashMap:
            if HashMap[key] == key:
                res = HashMap[key]
        
        return res
        