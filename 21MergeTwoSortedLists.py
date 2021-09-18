# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode()
        listhead = result
        while l1 != None and l2 != None:
            if l1.val >= l2.val:
                result.next = l2
                l2 = l2.next
            else:
                result.next = l1
                l1 = l1.next
            result = result.next
                
        if l1 != None:
            result.next = l1
        if l2 != None:
            result.next = l2
        return listhead.next
