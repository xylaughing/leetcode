class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums)-1
        while l < r:
            mid = (l+r)//2
            if nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]:
                return nums[mid]
            # single Element in left side
            if mid%2 == 0 and nums[mid] == nums[mid-1] or mid%2 != 0 and nums[mid] == nums[mid+1]:
                r = mid - 1
            elif mid%2 == 0 and nums[mid] == nums[mid+1] or mid%2 != 0 and nums[mid] == nums[mid-1]:              
                l = mid + 1
        return nums[l]
