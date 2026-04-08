# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        previous = None
        current = head
        while current:
            temp = current.next #node1
            current.next = previous #node0.next = None
            previous = current  # previous = node0 where node0.next = None
            current = temp # now current = node1 so loop will reach node1
        return previous




