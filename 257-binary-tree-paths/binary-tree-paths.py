# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def f(self,root , path, result):
        if not root:
            return
        path = path + '->' + str(root.val)    
        if not root.left and not root.right:
            result.append(path[2:])
            return
 
        
        self.f(root.left , path, result)
        self.f(root.right , path , result)
        return        

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        result = []
        self.f(root , '' , result)  
        return   result
        