# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        sizeA = 0
        sizeB = 0
        
        currA = headA
        currB = headB
        while currA:
            sizeA += 1
            currA = currA.next
            
        while currB:
            sizeB += 1
            currB = currB.next
            
        diff = abs(sizeA - sizeB)
        
        currA = headA
        currB = headB
        
        if sizeA < sizeB:
            while diff > 0:
                currB = currB.next
                diff -=1
        else:
            while diff > 0:
                currA = currA.next
                diff -=1
        while currA != None and currB != None:
            if currA == currB:
                return currA
            currA = currA.next
            currB = currB.next
        return None
        