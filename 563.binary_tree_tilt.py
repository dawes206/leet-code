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


    # def traveler(self, treeRoot, tilt):
    #     if not treeRoot: #if treeRoot is Null
    #         return 0
    #     if treeRoot.left:
    #         l = treeRoot.left
    #     if treeRoot.right:
    #         r = treeRoot.right
    #     node_tilt = abs(l.val - r.val)
    #
    #     self.traveler(l,traveled)
    #     self.traveler(r,traveled)
    #
    #     return traveled

    # def traveler(self,treeRoot,sum):
    #     if not treeRoot.left and not treeRoot.right: #if treeRoot has no left or right children
    #         print('sum: ', sum)
    #         print('node {} is bottom node'.format(treeRoot.val))
    #         node_tilt = 0
    #         value = treeRoot.val
    #         sum += treeRoot.val
    #         return node_tilt, sum #value #return a node_tilt value of 0 for bottom node, and the value of the bottom node
    #     l = treeRoot.left
    #     r = treeRoot.right
    #     sum += treeRoot.val
    #     node_tilt = abs(self.traveler(l,sum)[1] - self.traveler(r,sum)[1])
    #     print('the tilt for node {} is {}'.format(treeRoot.val, node_tilt))
    #     # node_val = treeRoot.val
    #     return node_tilt, sum #node_val

    def traveler(self, treeRoot, totalTilt):
        if not treeRoot.left and not treeRoot.right:
            print('node {} is bottom node'.format(treeRoot.val))
            return treeRoot.val

        l = treeRoot.left
        r = treeRoot.right
        print('current Node: ', treeRoot.val)
        print("totalTilt: ", totalTilt)
        left_child = self.traveler(l, totalTilt)
        right_child = self.traveler(r, totalTilt)
        node_tilt = abs(left_child - right_child)
        totalTilt[0] += node_tilt
        print('the tilt for node {} is {}'.format(treeRoot.val, node_tilt))

        return left_child + right_child + treeRoot.val

    def Tilt(self, treeRoot):
        tilt = [0]
        self.traveler(treeRoot,tilt)
        return tilt[0]



    # def traveler(self,treeRoot,tilt):
    #     if not treeRoot.left and not treeRoot.right:
    #         return 0
    #     l = treeRoot.left
    #     r = treeRoot.right
    #     left = self.traveler(l, tilt)
    #     right = self.traveler(r, tilt)
    #
    #     tilt[0] += abs(left-right)
    #
    #     return left+right+root.val





# Driver code
root = TreeNode(1)
root.left      = TreeNode(2)
root.right     = TreeNode(3)
root.left.left  = TreeNode(4)
root.left.right  = TreeNode(5)

test = Solution()
# print(test.traveler(root,0))
print(test.Tilt(root))
