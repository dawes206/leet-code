# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        answer = ListNode(None)
        temp = answer
        templ1 = l1
        templ2 = l2
        while templ1:
            temp.val = templ1.val + templ2.val
            temp.next = ListNode(None)
            temp = temp.next
            templ1 = templ1.next
            templ2 = templ2.next
        return(answer)




#for each value in provided list, l1.val = current value, l1.next = next value
number = [2,4,3]
head = ListNode(number[0])
temp = head
# head.next = ListNode(None)
# temp = head.next
for place in range(len(number)):
    if place != len(number)-1:
        temp.next = ListNode(None)
        temp.val = number[place]
        temp = temp.next
    else:
        temp.next = None
        temp.val = number[place]

number = [5,6,4]
head2 = ListNode(number[0])
temp2 = head2
# head.next = ListNode(None)
# temp = head.next
for place in range(len(number)):
    if place != len(number)-1:
        temp2.next = ListNode(None)
        temp2.val = number[place]
        temp2 = temp2.next
    else:
        temp2.next = None
        temp2.val = number[place]


test = Solution()
print(test.addTwoNumbers(head, head2).next.next.next.val)
# print(head.val, '->', head.next.val, '->',head.next.next.val)
