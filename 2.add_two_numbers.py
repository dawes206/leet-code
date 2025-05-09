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
        carryOver = False
        counter = 0
        while (templ1 or templ2) and counter<=5:
            temp.next = None
            if templ1 == None:
                temp.val = templ2.val
                templ2 = templ2.next
            elif templ2 == None:
                temp.val = templ1.val
                templ1 = templ1.next
            else:
                temp.val = templ1.val + templ2.val
                templ1 = templ1.next
                templ2 = templ2.next
            if carryOver == True:
                temp.val = temp.val + 1
                carryOver = False
            if temp.val >= 10:
                temp.val = temp.val - 10
                carryOver = True

            if templ1 == None and templ2 == None:
                temp.next = None
            else:
                temp.next = ListNode(None)
                temp = temp.next
            counter += 1
        return(answer)




#for each value in provided list, l1.val = current value, l1.next = next value
number = [4,3]
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
answer = test.addTwoNumbers(head,head2)
print(answer.val,
      answer.next.val,
      answer.next.next.val)
# print(head.val, '->', head.next.val, '->',head.next.next.val)
