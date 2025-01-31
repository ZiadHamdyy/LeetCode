# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        \\\
        Do not return anything, modify head in-place instead.
        \\\
        if not head or not head.next:
            return

        h = head

        while h and h.next and h.next.next:
            ptr = h
            while ptr.next and ptr.next.next:
                ptr = ptr.next

            last = ptr.next
            ptr.next = None

            last.next = h.next
            h.next = last

            h = last.next
        
