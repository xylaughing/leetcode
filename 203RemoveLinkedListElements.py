# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        newlist = ListNode()
        newhead = newlist

        if head is None:
            return newhead.next

        while head is not None:
            if head.val != val:
                newlist.next = head
                newlist = newlist.next
            else:   
                newlist.next = head.next
            head = head.next
        return newhead.next            
      
