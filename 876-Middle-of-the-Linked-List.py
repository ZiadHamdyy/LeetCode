# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr = head
        lenght = 0
        while ptr:
            ptr = ptr.next
            lenght += 1
        lenght = lenght // 2
        while lenght:
            head = head.next
            lenght -= 1
        return head