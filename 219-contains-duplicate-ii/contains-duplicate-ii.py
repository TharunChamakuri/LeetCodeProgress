class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        HashSet = set()
        leftInd = 0
        for rightInd in range(len(nums)):
            if rightInd - leftInd > k:
                HashSet.remove(nums[leftInd])
                leftInd += 1
            if nums[rightInd] in HashSet:
                return True
            HashSet.add(nums[rightInd])
        return False
                