# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        
        def helper(node , currSum):
            if not node:
                return False
            currSum += node.val
            if not node.left and not node.right and currSum == targetSum:
                return True
            return (helper(node.left , currSum) or helper(node.right , currSum))
        return helper(root , 0)
        