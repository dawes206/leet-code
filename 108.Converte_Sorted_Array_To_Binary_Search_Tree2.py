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
    def sortedArrayToBST(self, nums) -> TreeNode:
        if len(nums) == 0:
            return []
        root = TreeNode(0)
        dummy = root
        # print(id(root))
        self.make_subtree(dummy,nums)
        return root


    def make_subtree(self,node,l):
        # print(id(node))
        # if len(l) == 2:
        #     node.val = self.middle(l)
        #     node.left = TreeNode(l[0])
        #     return node
        # elif len(l) ==1:
        #     node.val = self.middle(l)
        #     return node
        if len(l)==0:
            node = None
            return node
        # print('id reassing?', id(node))
        node.left = TreeNode(None)
        node.right = TreeNode(None)
        node.left = self.make_subtree(node.left,l[0:round(len(l)/2)])
        node.right = self.make_subtree(node.right,l[round(len(l)/2)+1:])
        node.val = self.middle(l)
        # node = TreeNode(self.middle(l))
        return node


    def middle (self, l):
        return l[round(len(l)/2)]

test = Solution()
# ans = test.sortedArrayToBST([-10,-3,0,5,9])
ans = test.sortedArrayToBST([1,2,3,4,5,6,7,8,9])
ans.PrintTree()
# print(ans.left.left)
# print(ans.left.val)
