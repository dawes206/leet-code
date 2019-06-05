#          1
#       /     \
#     2         3
#   /   \     /   \
# 5       4  3      6
#
# is tilt 11-12
# or |4-5|+2 - |6-3|+3

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    #def findTilt(self, root: TreeNode) -> int:


    def traveler(self, treeRoot,traveled):
        traveled.append(treeRoot.val)
        if not treeRoot: #if treeRoot is Null
            return traveled
        if treeRoot.left:
            l = treeRoot.left
            self.traveler(l,traveled)
        if treeRoot.right:
            r = treeRoot.right
            self.traveler(r,traveled)
        return traveled





# Driver code
root = TreeNode(1)
root.left      = TreeNode(2)
root.right     = TreeNode(3)
root.left.left  = TreeNode(4)
root.left.right  = TreeNode(5)

test = Solution()
print(test.traveler(root,[]))
