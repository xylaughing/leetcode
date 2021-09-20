class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        swap_p = 0
        for check_p in range(0, len(nums)):
            if nums[check_p] != val:
                nums[swap_p] = nums[check_p]
                swap_p += 1
        return swap_p
