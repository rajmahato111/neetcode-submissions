# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        sentinal = ListNode(0)
        sentinal.next = head
        current = sentinal

        while current and current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        return sentinal.next    
