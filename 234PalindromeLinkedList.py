# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
      # convert Linked list to List
        l, i = [], 0
        while head:
            l.append(head.val)
            head = head.next

        while i <= len(l) // 2:
            if l[i] != l[len(l)-1-i]:
                return False
            else:
                i += 1
        return True
        
        
"""            
        l_rev = l[::-1]
        return l == l_rev
"""
