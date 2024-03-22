# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        if not head:
            return True
        
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
        
        secondHead = reverseList(slow)
        cur = head
            
        while secondHead:
            if secondHead.val != cur.val:
                return False
            secondHead = secondHead.next
            cur = cur.next
            
        return True
        
        