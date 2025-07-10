class Solution(object):
    def isHappy(self, n):
        
        HashMap = {}
        while n != 1:
            string = str(n)
            val = 0
            for digit in string:
                val += int(digit)**2
            n = val
            if val in HashMap:
                return False
            HashMap[val] = HashMap.get(val,0) + 1
        return True


        