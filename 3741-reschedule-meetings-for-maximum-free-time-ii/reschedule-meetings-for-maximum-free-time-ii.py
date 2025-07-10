class Solution(object):
    #Tharun
    def maxFreeTime(self, eventTime, startTime, endTime):
        freeTime = []
        freeTime.append(startTime[0])
        for i in range(1,len(startTime)):
            freeTime.append(startTime[i] - endTime[i-1])
        freeTime.append(eventTime - endTime[-1])

        maxLeft = [0] * len(freeTime)
        for i in range(1 , len(freeTime)):
            maxLeft[i] = max(maxLeft[i - 1],freeTime[i - 1])
        maxRight = [0] * len(freeTime)
        for i in range(len(freeTime)-2,-1,-1):
            maxRight[i] = max(maxRight[i + 1] , freeTime[i + 1])

        result = 0
        for i in range(1,len(freeTime)):
            currEventDuration = endTime[i - 1] - startTime[i - 1]
            if currEventDuration <= max(maxLeft[i - 1] , maxRight[i]):
                result = max(result ,freeTime[i - 1] + currEventDuration + freeTime[i])
            result = max(result , freeTime[i-1]+freeTime[i])
        return result

