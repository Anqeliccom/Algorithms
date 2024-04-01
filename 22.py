import re

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
    if not root:
        return "x"
    return f"({root.val}{serialize(root.left)}{serialize(root.right)})"

def deserialize(data):
    def des_help(data_list):
        while data_list:
            val = data_list.pop(0)
            if val == 'x':
                return None
            if val.isdigit():
                node = TreeNode(int(val))
                node.left = des_help(data_list)
                node.right = des_help(data_list)
                return node
            else:
                raise ValueError("Неверные входные данные")

    data_list = re.findall(r'\d+|x', data)
    return des_help(data_list)

# тесты
root = TreeNode(1)
root.left = TreeNode(3)
root.right = TreeNode(11)
root.left.left = TreeNode(5)
root.right.left = TreeNode(15)
root.right.right = TreeNode(13)

serialized_tree = serialize(root)
print("Сериализованное дерево:", serialized_tree)

deserialized_tree = deserialize(serialized_tree)
assert deserialized_tree.val == 1
assert deserialized_tree.left.val == 3
assert deserialized_tree.right.val == 11
assert deserialized_tree.left.left.val == 5
assert deserialized_tree.right.left.val == 15
assert deserialized_tree.right.right.val == 13

