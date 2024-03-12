# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        exitEarly = True
        
        
        while exitEarly:
            exitEarly = False
            nodeList = []
            cur = head
            while cur:
                if cur == head and cur.val == 0:
                    head = cur.next
                    exitEarly = True
                    break
                for i in range(len(nodeList)):
                    nodeList[i] = (nodeList[i][0], nodeList[i][1] + cur.val)
                    if nodeList[i][1] == 0:
                        if nodeList[i][0] == head:
                            head = cur.next
                        else:
                            nodeList[i-1][0].next = cur.next
                        exitEarly = True
                        break
                if exitEarly:
                    break
                if cur.val == 0:
                    nodeList[-1][0].next = cur.next
                    exitEarly = True
                    break
                nodeList.append((cur, cur.val))
                cur = cur.next
                    
            
        return head