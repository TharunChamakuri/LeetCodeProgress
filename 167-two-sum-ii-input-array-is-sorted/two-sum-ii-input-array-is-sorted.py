class Solution(object):
    def twoSum(self, numbers, target):
        HashMap = {}
        for i in range(len(numbers)):
            elem = target - numbers[i]
            if elem in HashMap:
                return[HashMap[elem]+1,i+1]
            else:
                HashMap[numbers[i]] = i
