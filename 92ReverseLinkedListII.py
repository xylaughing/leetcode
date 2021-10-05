# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        if left == right: return head
        stack, i = [], 1
        output = newhead = ListNode()
        while i < left:
            newhead.next = head
            head = head.next
            newhead = newhead.next
            i += 1
            
        while right >= i >= left:
            stack.append(head)
            head = head.next
            i += 1
        
        while stack:
            newhead.next = ListNode(stack.pop().val)
            newhead = newhead.next
            
        if head: newhead.next = head

        return output.next
        
