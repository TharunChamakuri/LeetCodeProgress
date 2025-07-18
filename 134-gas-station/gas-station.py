class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        if sum(cost) > sum(gas):
            return -1
        total , res = 0 , 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if total < 0:
                total = 0
                res = i + 1
        return res