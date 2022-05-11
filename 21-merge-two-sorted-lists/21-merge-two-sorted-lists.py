# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not l1:
            return l2
        
        if not l2:
            return l1
        
        pointer1, pointer2 = l1, l2
        
        head = l1
        
        if l1.val > l2.val:
            head = l2
            pointer2 = pointer2.next
        else:
            pointer1 = pointer1.next
        
        curPointer = head
            
        while pointer1 != None and pointer2 != None:
            if pointer1.val < pointer2.val:
                curPointer.next = pointer1
                pointer1 = pointer1.next
                curPointer = curPointer.next
            else:
                curPointer.next = pointer2
                pointer2 = pointer2.next
                curPointer = curPointer.next
                
        if not pointer1:
            curPointer.next = pointer2
        if not pointer2:
            curPointer.next = pointer1
                
        return head
    
        
        