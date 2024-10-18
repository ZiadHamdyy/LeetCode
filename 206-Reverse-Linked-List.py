# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        nextCur = None
        head = None
        while current:
            nextCur = current.next
            current.next = head
            head = current
            current = nextCur
        return head