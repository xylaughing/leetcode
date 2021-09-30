# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
       
        markhead = newlist = ListNode()
        cur_val = 101
        if head is None: return head
        while head.next is not None:
            if head.val != cur_val and head.val != head.next.val:
                newlist.next = ListNode(head.val)
                newlist = newlist.next
            else:
                cur_val = head.val
            head = head.next
        if head.val != cur_val:
            newlist.next = ListNode(head.val)
        
        return markhead.next
