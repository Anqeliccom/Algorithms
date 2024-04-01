from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def rightSideView(self, root):
        if not root:
            return []
        
        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)

            for i in range(level_size):
                node = queue.popleft()

                if i == level_size - 1:
                    result.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result


root = TreeNode(1)
root.left = TreeNode(3)
root.right = TreeNode(11)
root.left.left = TreeNode(5)
root.left.right = TreeNode(15)

solution = Solution()
print("Видимые узлы:")
print(solution.rightSideView(root))