class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        temp = [1]*n
        for i in range(len(nums)):
            ind = (i + k)%n
            temp[ind] = nums[i]
        for i in range(len(nums)):
            nums[i] = temp[i]