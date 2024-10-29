# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        string = ""
        ptr = head
        while ptr:
            string += str(ptr.val)
            ptr = ptr.next
        return int(string, 2)