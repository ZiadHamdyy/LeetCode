# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1, ptr2 = l1, l2
        li = ListNode()
        ptr = li
        remainder = 0
        while ptr1 or ptr2:
            if ptr1 == None:
                num1 = 0
                num2 = ptr2.val
            elif ptr2 == None:
                num1 = ptr1.val
                num2 = 0
            else:
                num1 = ptr1.val
                num2 = ptr2.val

            if num1 + num2 + remainder > 9:
                sum = (num1 + num2 + remainder) % 10
                ptr.next = ListNode(sum)
                ptr = ptr.next
                remainder = ((num1 + num2 + remainder) - sum) // 10
            else:
                sum = num1 + num2 + remainder
                ptr.next = ListNode(sum)
                remainder = 0
                ptr = ptr.next
            if ptr1:
                ptr1 = ptr1.next
            if ptr2:
                ptr2 = ptr2.next
        if remainder:
            ptr.next = ListNode(remainder)
        li = li.next
        return li
        