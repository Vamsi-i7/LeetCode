# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        if root == None: return TreeNode(val)
        temp = root
        while temp != None:
            if val < temp.val:
                if temp.left == None:
                    temp.left = TreeNode(val); break
                temp = temp.left
            else:
                if temp.right == None:
                    temp.right = TreeNode(val); break
                temp = temp.right
        return root
        