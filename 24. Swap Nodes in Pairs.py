# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #if not head or not head.next: return head
        ct, record = 0, 0
        pointer = head
        while pointer and pointer.next:
            if ct%2 == 0: 
                record = pointer.val
                pointer.val = pointer.next.val
            else:
                pointer.val = record
            pointer = pointer.next
            ct += 1
        if ct%2 != 0: pointer.val = record
        return head
