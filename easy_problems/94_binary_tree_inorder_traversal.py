class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder_traversal(self, root: TreeNode | None) -> list:
    if root is None:
        return []
    res = []
    if root.left:
        res.extend(self.inorderTraversal(root.left))

    res.append(root.val)

    if root.right:
        res.extend(self.inorderTraversal(root.right))

    return res
