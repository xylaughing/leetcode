# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """        
        if head is None: return False
        while head:
            if head.val == None:
                return True
            head.val = None
            head = head.next
        return False
