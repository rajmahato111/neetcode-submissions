# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    # store all element of node B in hashset
        visited = set()
        while headB:
            visited.add(headB)
            headB = headB.next
    # seach one by one of node A element in node B
        while headA:
            if headA in visited:
                return headA
            headA = headA.next
        return None