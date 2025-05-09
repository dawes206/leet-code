# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
#
# Example:
#
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#Thoughts
# go trhough each list together. For each node, assign the next attribute to the next node in the other list
# L      R
# 1      1
# |      |
# 2      3
# |      |
# 4      4
#newL = ListNode(l1.val)
# helper function will do the recursion
#SEt value of current newLnode.next to each new value in L and R that is traversed




# class Solution:
#     def helper(self, newLNode, lnode ,rnode):
#         if not rnode and not lnode:
#             return newLNode
#         newLNode.next = ListNode(rnode.val)
#         newLNode.next.next = ListNode(lnode.val)
#         lnode = lnode.next
#         rnode = rnode.next
#         return self.helper(newLNode.next.next, lnode, rnode)
#
#     # def helper(self, node, lnode, rnode):
#     #     node.next = ListNode(rnode.val)
#     #     node.next.next = ListNode(lnode.val)
#     #     return (node)
#
#
#     def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
#         newL = ListNode(l1.val)
#         newList = self.helper(newL, l1, l2)
#         return newList
#
# L = ListNode(1)
# L.next = ListNode(2)
# L.next.next =ListNode(4)
# R = ListNode(1)
# R.next = ListNode(3)
# R.next.next = ListNode(4)
#
# test = Solution()
# ans = test.mergeTwoLists(L,R)
#
# print(ans.val.next)



# iterative
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# class Solution:
#     def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
#         if not l1 and not l2:
#             return ListNode(None)
#         elif not l1:
#             return l2
#         elif not l2:
#             return l1
#         newList = ListNode(l1.val)
#         while l1 and l2:
#             newList.next = ListNode(l2.val)
#             newList.next.next = ListNode(l1.val)
#             newList = newList.next.next
#             l2 = l2.next
#             l1 = l1.next
#             print(newList.val)
#         while not l1:
#             if not l2:
#                 print('here')
#                 return newList
#             newList.next = ListNode(l2.val)
#             newList = newList.next
#             l2 = l2.next
#         while not l2:
#             if not l1:
#                 return newList
#             newList.next = ListNode(l1.val)
#             newList = newList.next
#             l1 = l1.next
#         return newList

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        newList = dummy
        if not l1 and not l2:
            return ListNode(None)
        elif not l1:
            return l2
        elif not l2:
            return l1
        # newList = ListNode(l1.val)
        while l1 or l2:
            if not l2:
                newList.next = l1
                l1 = l1.next
            elif not l1:
                newList.next = l2
                l2 = l2.next
            else:
                newList.next = l2
                newList.next.next = l1.next
                newList = newList.next.next
                l2 = l2.next
                l1 = l1.next

            newList = newList.next
            return dummy


#
# L = ListNode(1)
# L.next = ListNode(2)
# L.next.next =ListNode(4)
# R = ListNode(1)
# R.next = ListNode(3)
# R.next.next = ListNode(4)
#
# test = Solution()
# ans = test.mergeTwoLists(L,R)
#
# print(ans.next)

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# class Solution:
#     def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
#         dummy = ListNode(0)
#         newList = dummy
#         self.merge(newList, l1, l2)
#         return dummy.next
#
#     def merge(self, newList, l1, l2):
#         while l1 or l2: #while either l1 or l2 is true
#             if not l1: # if l1 is None
#                 newList.next = l2
#                 l2 = l2.next
#             elif not l2: #if l2 is none
#                 newList.next = l1
#                 l1 = l1.next
#             elif l1.val < l2.val: #if
#                 newList.next = l1
#                 l1 = l1.next
#             else:
#                 newList.next = l2
#                 l2 = l2.next
#             newList = newList.next


L = ListNode(1)
L.next = ListNode(2)
L.next.next =ListNode(4)
R = ListNode(1)
R.next = ListNode(3)
R.next.next = ListNode(4)

test = Solution()
ans = test.mergeTwoLists(L,R)
#
while ans:
    print(ans.val)
    ans=ans.next
# print(ans.val)
# print(ans.next.val)
# print(ans.next.next.val)
