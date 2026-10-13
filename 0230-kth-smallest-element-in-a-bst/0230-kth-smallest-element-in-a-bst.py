# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        self.c  = 0
        self.res = None

        def sol(root):
            if root is None : return 
            sol(root.left)
            self.c += 1
            if self.c  == k:
                self.res = root
                return
            sol(root.right)
        sol(root)
        return self.res.val
        
        