# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    def isBalance(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        lh = self.isBalance(root.left)
        rh = self.isBalance(root.right)

        if lh == -1 or rh == -1:
            return -1

        if abs(lh- rh)>1 :
            return -1

        return 1 + max(lh, rh)   

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ans = self.isBalance(root)
        return ans != -1  

        