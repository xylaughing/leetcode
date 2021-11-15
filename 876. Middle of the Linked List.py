# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """"""
        st, i = [], 0
        while head:
            st.append(head)
            head = head.next
            i += 1
        i = (i-1) // 2
        while i > 0:
            st.pop()
            i -= 1
        return st.pop()
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
