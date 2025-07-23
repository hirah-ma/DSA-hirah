from collections import deque, defaultdict

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque([(root, 0)])
        level_map = defaultdict(list)

        while q:
            node, level = q.popleft()
            level_map[level].append(node.val)

            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))

        result = []
        for level in range(len(level_map)):
            values = level_map[level]
            if level % 2 != 0:
                values.reverse()
            result.append(values)

        return result
