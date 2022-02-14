# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0, head)
        
        while head and head.next:
            # find the node to be inserted.
            if head.val > head.next.val:
                tobeInserted = head.next
                #find the node pos to insert
                prev = dummy
                while prev.next.val < tobeInserted.val:
                    prev = prev.next
                # insert tobeinserted after prev
                head.next = tobeInserted.next
                tobeInserted.next = prev.next
                prev.next = tobeInserted
            else:
                head = head.next
        return dummy.next
