# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        a1, b1 = list1, list1
        
        for i in range(a-1):
            a1 = a1.next
            
        for i in range(b+1):
            b1 = b1.next
            
        list2end = list2
        
        while list2end.next != None:
            list2end = list2end.next
            
        
        a1.next = list2
        
        list2end.next = b1
        
        return list1
        
        