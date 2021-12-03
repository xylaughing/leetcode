# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        """
        amount, stack = 0, deque([])
        while head:
            stack.append(head.val)
            amount += 1
            head = head.next
    
        ct, new = 0, ListNode(0)    
        res = new
        while ct < amount:
            if ct == amount - n:
                stack.popleft()
            else:
                new.next = ListNode(stack.popleft())
                new = new.next
            ct += 1
        return res.next
        """
        new = res = head 
        amount, i = 0, 0
        while head:
            amount += 1
            head = head.next
        if amount == n: return new.next
        while i < amount - n - 1:
            new = new.next
            i += 1
        new.next = new.next.next
        return res
