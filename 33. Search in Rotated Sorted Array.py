class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        """
        l, r = 0, len(nums)-1
        if l == r: return 0 if target == nums[0] else -1
        if nums[r] < target < nums[l]:
            return -1
        if nums[l] > nums[r] and target >= nums[l]:
            while nums[r] > nums[r-1]:
                r -= 1
            r -= 1
        elif nums[l] > nums[r] and target <= nums[r]:
            while nums[l] < nums[l+1]:
                l += 1
            l += 1
            
        while l < r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                l = mid + 1
            else:
                r = mid 
        return l if nums[l] == target else -1
        """
        l, r = 0, len(nums)-1
        if nums[l] == target: return l
        if nums[r] == target: return r
        while l < r:
            mid = (l+r) // 2
            # nums[mid] and target in same side.
            if (nums[mid] > nums[0]) == (target > nums[0]):
                if target == nums[mid]:
                    return mid
                elif target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid
            elif target < nums[0]:
                l = mid + 1
            else:
                r = mid
        return l if nums[l] == target else -1
