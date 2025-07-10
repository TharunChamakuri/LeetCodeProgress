class Solution:
    def findLHS(self, nums: List[int]) -> int:
        Maxres = 0
        HashMap = Counter(nums)
        
        for k in HashMap:
            if k-1 in HashMap:
                res = HashMap[k] + HashMap[k-1]
                Maxres = max(res,Maxres)
        return Maxres

                
