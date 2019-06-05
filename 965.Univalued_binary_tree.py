# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def traveler(self, treeRoot):
        if not treeRoot:
            return True
        if not treeRoot.left and not treeRoot.right:
            return True
        if treeRoot.val != treeRoot.left.val or treeRoot.val != treeRoot.right.val:
            return False
        else:
            left = self.traveler(treeRoot.left)
            right = self.traveler(treeRoot.right)
            if left and right:
                return True
            else:
                return False

    # def helper(self, root):
    #     num = [0]
    #     self.traveler(root, num)
    #     return num[0]


# Driver code
root = TreeNode(2)
root.left      = TreeNode(2)
root.right     = TreeNode(2)
root.left.left  = TreeNode(2)
root.left.right  = TreeNode(2)
root.right.right = TreeNode(2)
root.right.left = None

test = Solution()
print(test.traveler(root))
# print(test.helper(root))
# print(root.right.left.val)
