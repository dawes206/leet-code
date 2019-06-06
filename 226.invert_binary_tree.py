#     4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
#
#     4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        lRoot = root.left
        rRoot = root.right
        left = self.invertTree(lRoot)
        right = self.invertTree(rRoot)
        return



    def traverse(self,root, touched):
        if not root:
            return
        print(root.val)
        touched.append(root.val)
        lRoot = root.left
        rRoot = root.right
        left = self.traverse(lRoot, touched)
        right = self.traverse(rRoot, touched)
        return touched

    # def traverse_bfs(self,root,touched):
    #     if not root:
    #         return
    #     touched += [root.val]


# Driver code
#         1
#       /   \
#     2       3
#   /   \       \
# 4      5       6

root = TreeNode(1)
root.left      = TreeNode(2)
root.right     = TreeNode(3)
root.left.left  = TreeNode(4)
root.left.right  = TreeNode(5)
root.right.right = TreeNode(6)
root.right.left = None

test = Solution()
print(test.traverse(root, []))
