class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def get_sorted(self, root):
        stack = []
        sorted_nodes = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            sorted_nodes.append(root)
            root = root.right
        return sorted_nodes

    def build_bst(self, nodes, start, end):
        if start > end:
            return None

        mid = (start + end) // 2
        root = nodes[mid]
        root.left = self.build_bst(nodes, start, mid - 1)
        root.right = self.build_bst(nodes, mid + 1, end)
        return root

    def balanceBST(self, root):
        nodes = self.get_sorted(root)
        return self.build_bst(nodes, 0, len(nodes) - 1)

def test_balanceBST():
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(8)
    root.right.left.left = TreeNode(5)
    root.right.right.right = TreeNode(9)

    expected_result = TreeNode(7)
    expected_result.left = TreeNode(4)
    expected_result.right = TreeNode(8)
    expected_result.right.right = TreeNode(9)
    expected_result.left.left = TreeNode(2)
    expected_result.left.right = TreeNode(6)
    expected_result.left.right.left = TreeNode(5)

    solution = Solution()
    balanced_tree = solution.balanceBST(root)

    def tree_to_list(node):
        if not node:
            return []
        return tree_to_list(node.left) + [node.val] + tree_to_list(node.right)
    
    assert tree_to_list(balanced_tree) == tree_to_list(expected_result)

    print("Тест пройден успешно!")

test_balanceBST()