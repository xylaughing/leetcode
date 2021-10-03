# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        # convert sorted List to Array
        def ListToArray(listnode):
            arr = []
            while listnode:
                arr.append(listnode.val)
                listnode = listnode.next
            return arr
        
        # concert sorted array to BTS   
        def sortedArrayToBST(nums):
            output = TreeNode(nums[len(nums)//2])
            if 1 < len(nums) <= 3:
                output.left = TreeNode(nums[0])
            if len(nums) == 3:
                output.right = TreeNode(nums[2])
            elif len(nums) > 3:
                    output.left = sortedArrayToBST(nums[0 : len(nums)//2])
                    output.right = sortedArrayToBST(nums[len(nums)//2 + 1 : len(nums)])
            return output
    
        if head is None: return None
        return sortedArrayToBST(ListToArray(head))
