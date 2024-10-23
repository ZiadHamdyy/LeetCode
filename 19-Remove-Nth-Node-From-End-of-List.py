# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ptr = head
        counter = 0
        while ptr:
            counter += 1
            ptr = ptr.next
        counter -= n
        ptr = head
        for _ in range(counter - 1):
            ptr = ptr.next
        if counter == 0:
            ptr = ptr.next
            head = ptr
        elif ptr and ptr.next:
            ptr.next = ptr.next.next
        else:
            ptr = None
            head = ptr
        return head