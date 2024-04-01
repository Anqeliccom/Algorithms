class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root):
        if not root:
            return True
        
        stack = [(root, float('-inf'), float('inf'))] 
        
        while stack:
            node, min_val, max_val = stack.pop()
            
            if not node:
                continue
                
            if node.val <= min_val or node.val >= max_val:
                return False
            
            stack.append((node.right, node.val, max_val))
            stack.append((node.left, min_val, node.val))
        
        return True
        
root = TreeNode(5)
root.left = TreeNode(2)
root.right = TreeNode(10)
root.left.left = TreeNode(1)
root.left.right = TreeNode(4)
root.right.right = TreeNode(12)

solution = Solution()

if solution.isValidBST(root):
    print("Это дерево - бинарное дерево поиска.")
else:
    print("Это дерево - не бинарное дерево поиска.")