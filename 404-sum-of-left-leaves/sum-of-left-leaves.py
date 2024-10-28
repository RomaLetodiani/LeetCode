# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        res = [0]

        self.helper(root,res,False)

        return res[0]

    def helper(self, root, res, isLeft):
        if not root:
            return

        if isLeft and not root.left and not root.right:
            res[0] += root.val

        self.helper(root.left, res, True)
        self.helper(root.right, res, False)
        