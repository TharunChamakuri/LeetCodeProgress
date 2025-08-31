class Solution(object):
    def areaOfMaxDiagonal(self, dimensions):
        HashMap = {}
        maxarea = 0
        for i , rectangle in enumerate(dimensions):
            l , w = rectangle
            HashMap[i] = max(HashMap.get(i , 0) , math.sqrt(l*l + w*w))
            maxarea = max(maxarea , HashMap[i])

        res = []
        for key in HashMap:
            if HashMap[key] == maxarea:
                res.append(dimensions[key][0] * dimensions[key][1])
        return max(res)
        
                