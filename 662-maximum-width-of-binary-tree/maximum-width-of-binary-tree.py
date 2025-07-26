# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root :
            return 0
        q = [(root,0)]
        ans = 0
        while q:
            node , curri =q[0]
            l = len(q)
            first = 0 
            last = 0
            for i in range(l):
                
                node, curri = q.pop(0)
                              
                if i==0:
                    first = curri
                if i == l-1:
                    last = curri
                if node.left:
                    q.append((node.left, 2*curri + 1) )
                if node.right:
                    q.append((node.right , 2*curri +2))

            ans =  max( ans , last - first +1)               
        return ans

        