# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        stack = []
        while head:
            stack.append(head)
            head = head.next
        
        output = newhead = ListNode()
        while stack:
            newhead.next = ListNode(stack.pop().val)
            newhead = newhead.next
    
        return output.next
