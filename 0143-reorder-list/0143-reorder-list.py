# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def reverseList(head):
            prev = None
            cur = head
        
            while cur:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp

            return prev
        
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        if fast:
            slow = slow.next
        
        h2 = reverseList(slow)
        h1 = head
        
        while True:
            temp1 = h1.next
            
            h1.next = h2
            h1 = temp1
            
            if not h2:
                break
            
            temp2 = h2.next
            h2.next = h1
            h2 = temp2
            
            if not h1:
                break