class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, r = 0, len(nums)-1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] == target:
                break
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        if l == r:
            return [l,r] if nums[l] == target else [-1,-1]
        elif l > r: 
            return [-1,-1]
        l = r = mid
        while l > 0 and nums[l-1] == target:
            l -= 1
        while r < len(nums)-1 and nums[r+1] == target:
            r += 1
        return [l, r]
