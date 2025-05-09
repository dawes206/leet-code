class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.val),
        if self.right:
            self.right.PrintTree()

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        node = root
        to_visit = []
        to_visit.append(node)
        while to_visit:
            node = to_visit.pop(0)
            if node:
                to_visit.append(node.left)
                to_visit.append(node.right)
                # print('left before', node.left)
                # print('right before', node.right)
                dummy = node.left
                node.left = node.right
                node.right = dummy
                # print('left after', node.left)
                # print('right after', node.right)
        return root





root = TreeNode(1)
root.left      = TreeNode(2)
root.right     = TreeNode(3)
root.left.left  = TreeNode(4)
root.left.right  = TreeNode(5)
root.right.right = TreeNode(6)
root.right.left = None

test = Solution()
ans = test.invertTree(root)

ans.PrintTree()
