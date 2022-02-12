# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        chead = head
        stack = []
        while chead:
            stack.append(chead)
            chead = chead.next
        n = len(stack) // 2
        mid = stack.pop(n)
        
        #step 2: reverse second half
        prev, curr = None, mid.next
        while curr:
            nextt = curr.next
            curr.next = prev
            prev = curr
            curr = nextt    
        mid.next = None
        
        #step 3: merge lists
        head1, head2 = head, prev
        while head2:
            nextt = head1.next
            head1.next = head2
            head1 = head2
            head2 = nextt
            
