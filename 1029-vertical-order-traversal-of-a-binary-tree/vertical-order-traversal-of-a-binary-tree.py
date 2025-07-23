from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        d = defaultdict(list)
        q = [(root, 0, 0)]  # node, vertical_level, level
        while q:
            node, vl, level = q.pop(0)
            d[vl].append((level, node.val))  # ⬅️ key change here

            if node.left:
                q.append((node.left, vl - 1, level + 1))
            if node.right:
                q.append((node.right, vl + 1, level + 1))

        ans = []
        for key in sorted(d.keys()):
            # sort by level first, then value
            col = sorted(d[key])
            ans.append([val for lvl, val in col])
        return ans
            

        
        