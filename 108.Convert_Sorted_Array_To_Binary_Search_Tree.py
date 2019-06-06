# Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
#
# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
#
# Example:
#
# Given the sorted array: [-10,-3,0,5,9],
#
# One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:
#
#       0
#      / \
#    -3   9
#    /   /
#  -10  5

#if you have binary tree of height h, you need 2^h-1 values. h = log(len(nums)+1)/log(2)
#I can create a tree and then traverse it and assign values.
#I can create a tree and assign values as I create it.
#I will create tree and them populate
#If I utilize a queue I can look at the root, create left and right children add left and right to my queue, then create children for each node in my Queue
#every time I populate the left and right attributes of a node, I can add 1 to number, and when number = len(nums), stop the process. The q faciliates breadth first. The number will cause base case

# Creating tree
#iterative
# [0,0,0,0,0]
# queue.enqueue(TreeNode(None))
# while number <= len(nums)
# node = queue.dequeue()
# node.left = TreeNode(None)
# node.right = TreeNode(None)
# queue.enqueue(node.left)
# queue.enqueue(node.right)
# number += 2



#recursive
# def helper(self, length, number, queue): #length is length of input list
#     if number>length-1:
#          return
#     else:
#         node = queue.dequeue()
#         node.left = TreeNode(None)
#         node.right = TreeNode(None)
#         queue.enqueue(node.left)
#         queue.enqueue(node.right)
#         number += 2
#         self.helper(length, number, queue)
#
# #populating tree
# #recursive
# def dfs(self, number, nums):
#     if not node.left and not node.right: #if node has no children assigned
#         node.val = nums[number]
#         number +=1
#         return
#     else:
#         self.dfs(number, nums)


#iterative
# stack.push(root) #a stack so you can see the most recent node you've traversed (parent) and choose it's other child
# while number <= len(nums)
#     if not node.left and not node.right:
#         node.val = nums[number]
#         number += 1
#         node = stack.pop()
#     elif not node.left or not node.right: #if either childe empty
#         node = node.right
#     elif node.right: #if right child filled
#         node =
#
#     else:
#         stack.push(node) #Add node to stack to go back to it after we fill it's left child
#         node = node.left







# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# List = [-10,-3,0,5,9]


class Solution:
    def sortedArrayToBST(self, nums) -> TreeNode:
        root = TreeNode(None)
        queue = []
        # queue.enqueue(root)
        queue.append(root)
        self.helper(root, len(nums), 0, queue)
        self.dfs(root, 0, nums)
        return root


    def helper(self, node, length, number, queue): #length is length of input list
        if number>length-1:
             return
        else:
            # node = queue.dequeue()
            # print(len(queue))
            node = queue.pop(0)
            node.left = TreeNode(None)
            node.right = TreeNode(None)
            # queue.enqueue(node.left)
            # queue.enqueue(node.right)
            queue.append(node.left)
            queue.append(node.right)
            number += 2
            self.helper(node, length, number, queue)

    def dfs(self, node, number, nums):
        if not node.left and not node.right: #if node has no children assigned (leaf)
            node.val = nums[number]
            number +=1
            return
        elif node.left.val and not node.val: #if left child has value but node has no value, assign value to node
            node.val = nums[number]
            number +=1
            return
        elif node.left.val and node.val and not node.right.val: #if both left child and node has value, assign value to right child (through dfs)
            print('here')
            self.dfs(node.right,number,nums)
        else: #left, right, and node have value
            return


test = Solution()
ans = test.sortedArrayToBST([-10,-3,0,5,9])
print(ans.val)
# print(ans.left.val)
# print(ans.right.val)
# print(ans.left.left.val)
# print(ans.left.right.val)
# print(ans..val)
# print(ans..val)
# print(ans..val)
# print(ans..val)
# print(ans..val)
# print(ans..val)
# print(ans..val)

# print(ans.left.left)
# print(ans)
# def graph_print(ans):
#     global visited
#     if node not in visited:
#         visited.append(node)
#         for n in graph[node]:
#             dfs(graph,n)
# print(ans)
# graph_print(ans)
# print(visited)
