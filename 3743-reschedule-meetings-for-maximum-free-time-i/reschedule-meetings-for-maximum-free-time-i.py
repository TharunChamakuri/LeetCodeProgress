class Solution(object):
    def maxFreeTime(self, eventTime, k, startTime, endTime):
        freeTime = []
        freeTime.append(startTime[0] - 0)
        for i in range(1,len(startTime)):
            freeTime.append(startTime[i] - endTime[i - 1])
        freeTime.append(eventTime - endTime[-1])

        i , j = 0 , 0
        currSum , MaxSum = 0 , 0
        while j < len(freeTime):
            currSum += freeTime[j]
            if i < len(freeTime) and j - i + 1 > k + 1:
                currSum -= freeTime[i]
                i += 1
            MaxSum = max(MaxSum , currSum)
            j += 1
        return MaxSum

        