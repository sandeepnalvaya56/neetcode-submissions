# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # both lists are merged
        # if both lists do not have any values, return None
        if not list1 and not list2:
            print("returned here at no list found")
            return None
        elif not list1:
            return list2
            print("list1 not found. list2 returned")
        elif not list2:
            return list1
            print("list2 not found. list1 returned")
        else:
            current_l1 = list1
            current_l2 = list2
        
        # identify the head
        if current_l1.val <= current_l2.val:
            final_head = ListNode(current_l1.val, None)
            current_l1 = current_l1.next
        else:
            final_head = ListNode(current_l2.val, None)
            current_l2 = current_l2.next
        
        final = final_head
        # Now we will traverse the "current_l1" - We can chose any one until it exhausts, once exhausted we will simply attach the other remaining one and return the output
        counter = 1
        while current_l1:
            if not current_l2:
                print("Current L2 Found Empty. Setting final.next as current_l1")
                final.next = current_l1
                return final_head
            
            if current_l1.val <= current_l2.val:
                final.next = current_l1
                current_l1 = current_l1.next #move current_l1 pointer
                final = final.next #move final pointer
            else:
                final.next = current_l2
                current_l2 = current_l2.next #move current_l2 pointer
                final = final.next #move final pointer
            
        if not current_l1 and current_l2:
                final.next = current_l2
                return final_head
 