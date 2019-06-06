
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isUnivalTree(self, root):
        left_correct = (not root.left or root.val == root.left.val
                and self.isUnivalTree(root.left))
        right_correct = (not root.right or root.val == root.right.val
                and self.isUnivalTree(root.right))
        return left_correct and right_correct

    # def isUniversalTree(self,root):
    #     if (root.val == root.left.val and self.isUniversalTree(root.left)) or not root.left:
    #         return True
    #     if (root.val == root.right.val and self.isUniversalTree(root.right)) or not root.right:
    #         return True
    #


# Driver code
root = TreeNode(2)
root.left      = TreeNode(2)
root.right     = TreeNode(2)
root.left.left  = TreeNode(2)
root.left.right  = TreeNode(2)
root.right.right = TreeNode(2)
root.right.left = None

test = Solution()
print(test.isUnivalTree(root))
