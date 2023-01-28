# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
pre = None
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        global pre
        pre = None
        return self.inorder(root)

    def inorder(self, cur):
        global pre
        if not cur:
            return True
        if not self.inorder(cur.left):
            return False
        if pre:
            if cur.val <= pre.val:
                return False
        pre = cur
        return self.inorder(cur.right)
