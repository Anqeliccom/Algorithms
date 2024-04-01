class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def trimBST(self, root, low, high):
        if not root:
            return None
        
        while root and (root.val < low or root.val > high):
            if root.val < low:
                root = root.right
            else:
                root = root.left
        
        if root:
            root.left = self.trimBST(root.left, low, high)
            root.right = self.trimBST(root.right, low, high)
        
        return root

root = TreeNode(9)
root.left = TreeNode(4)
root.right = TreeNode(14)
root.left.left = TreeNode(2)
root.left.right = TreeNode(6)
root.right.right = TreeNode(17)

solution = Solution()
trimmed_root = solution.trimBST(root, 3, 13)

# Вывод
def serialize(root):
    if not root:
        return "x"
    return f"({root.val}{serialize(root.left)}{serialize(root.right)})"

print("Дерево после удаления:")
print(serialize(trimmed_root))
