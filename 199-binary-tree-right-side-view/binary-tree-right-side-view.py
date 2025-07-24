from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        d = defaultdict(list)
        if not root:
            return []
        q = [(root , 0)]
        
        while q:
            cur , hl =  q.pop(0)
            d[hl].append(cur.val)
            if cur.left:
                q.append((cur.left,hl+1))
            if cur.right:
                q.append((cur.right, hl+1))
        result = []        
        for key in sorted(d.keys()) :
            result.append(d[key][-1])
        return result               


        