class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        for x, y in Counter(nums).items():
            if y > 1: 
                return x        
        """
        slow, fast = nums[0], nums[nums[0]] 
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        fast = 0
        while fast != slow:
            fast = nums[fast]
            slow = nums[slow]
        return fast
