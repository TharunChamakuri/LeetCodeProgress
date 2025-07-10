from typing import List

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # Store (index, value) pairs
        temp = [[i, nums[i]] for i in range(len(nums))]
        
        # Sort by value descending to get largest k elements
        temp.sort(key=lambda x: x[1], reverse=True)
        
        # Take top k elements
        top_k = temp[:k]
        
        # Sort top_k by index to preserve original order
        top_k.sort(key=lambda x: x[0])
        
        # Extract values in original order
        res = [x[1] for x in top_k]
        return res
