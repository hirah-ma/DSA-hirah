# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = - float('inf')
    
    def f(self, root):
        if not root:
            return 0
        lh = self.f(root.left)
        rh = self.f(root.right)
        lh = lh if lh > 0 else 0
        rh = rh if rh > 0 else 0

        
        self.ans = max(self.ans, root.val + (lh+rh) )


        return root.val + max(lh,rh)    
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = root.val
        self.f(root)
        return int(self.ans)
        