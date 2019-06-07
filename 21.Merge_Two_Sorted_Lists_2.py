class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        left = l1
        right = l2
        root = ListNode(None)
        node = root
        while left and right:
            if left.val<=right.val:
                node.next = left
                left = left.next
            else:
                node.next = right
                right = right.next
            node = node.next
        if left:
            print('left is not none')
            node.next = left
        elif right:
            print('right is not none')
            node.next = right
        return root.next


L = ListNode(1)
L.next = ListNode(2)
L.next.next =ListNode(4)
R = ListNode(1)
R.next = ListNode(3)
R.next.next = ListNode(4)


test = Solution()
ans = test.mergeTwoLists(L,R)
print(ans)
mover = ans
while mover:
    print('Node: ', mover.val)
    mover = mover.next
