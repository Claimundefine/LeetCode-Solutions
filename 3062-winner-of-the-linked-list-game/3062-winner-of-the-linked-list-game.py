# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gameResult(self, head: Optional[ListNode]) -> str:
        count = 0
        
        cur = head
        
        while cur is not None:
            if cur.val > cur.next.val:
                count += 1
            else:
                count -= 1
            cur = cur.next.next
            
        if count < 0:
            return "Odd"
        elif count > 0:
            return "Even"
        
        return "Tie"