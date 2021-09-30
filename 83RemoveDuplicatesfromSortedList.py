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
        markhead = head
        while head:
            temp = head
            while head.next is not None and head.val == head.next.val:
                head = head.next
            temp.next = head.next
            head = head.next

        return markhead
