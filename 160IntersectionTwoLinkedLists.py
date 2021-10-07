# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        pointerA, pointerB = headA, headB
        if pointerA == None or pointerB == None:
            return null
        
        while pointerA != pointerB:
            if pointerA == None:    pointerA = headB
            else:   pointerA = pointerA.next
            if pointerB == None:    pointerB = headA
            else: pointerB = pointerB.next
        return pointerA
        
