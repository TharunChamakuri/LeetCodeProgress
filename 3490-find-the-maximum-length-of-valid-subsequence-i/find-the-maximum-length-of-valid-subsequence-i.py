class Solution(object):
    def maximumLength(self, nums):
        evenCount , oddCount , alternativeCount = 0 , 0 , 0
        parity = nums[0] % 2
        if parity == 1:
            oddCount += 1
        else:
            evenCount += 1

        for i in range(1,len(nums)):
            currParity = nums[i] % 2
            if currParity == 1:
                oddCount += 1
            elif currParity == 0:
                evenCount += 1
            if currParity != parity:
                alternativeCount += 1
                parity = currParity
        return max(oddCount , evenCount , alternativeCount + 1)

        