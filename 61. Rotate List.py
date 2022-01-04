# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k == 0: return head
        res = newhead = head
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        k = k%len(stack)
        if k==0: return res
        stack = stack[-k:] + stack[0:len(stack)-k]
        for i in range(len(stack)):
            newhead.next = ListNode(stack[i])
            newhead = newhead.next
        return res.next
