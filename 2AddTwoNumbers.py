# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        tail = head = ListNode()
        add = 0
        while l1 or l2:
            if l1 is None:
                temp = l2.val + add
                tail.next = ListNode(int(temp % 10))
                tail = tail.next
                l2 = l2.next                
            else: 
                if l2 is None:
                    temp = l1.val + add
                    tail.next = ListNode(int(temp % 10))
                    tail = tail.next
                    l1 = l1.next   
                else:   
                    temp = l1.val + l2.val + add
                    tail.next = ListNode(int(temp % 10))
                    tail = tail.next
                    l1 = l1.next
                    l2 = l2.next                    
                    
            if temp >= 10:  add = 1
            else:   add = 0
            print("temp=",temp, "add=", add)            
        if add == 1: tail.next = ListNode(1)
        return head.next
            
