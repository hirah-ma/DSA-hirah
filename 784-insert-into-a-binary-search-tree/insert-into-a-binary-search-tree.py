# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]: 
        def insert(root, val):
            if not root:
                root=TreeNode(val=val)
                return root
            if root.val > val:
                root.left = insert(root.left, val)
            if root.val < val:    
                root.right = insert(root.right, val) 
            return root
        return insert(root,val)           
        