# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1 = list1
        ptr2 = list2
        start = ListNode()
        ptr = start
        while ptr1 != None and ptr2 != None:
            if ptr1.val <= ptr2.val:
                ptr.next = ptr1
                ptr1 = ptr1.next
                ptr = ptr.next
            else:
                ptr.next = ptr2
                ptr2 = ptr2.next
                ptr = ptr.next
        if ptr1 != None:
            ptr.next = ptr1
        if ptr2 != None:
            ptr.next = ptr2
        start = start.next
        return start