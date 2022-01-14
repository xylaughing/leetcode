class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        l, r = 0, len(nums)-1    
        while l < r:
            while l < r and nums[l] == nums[r]:
                if nums[l] == target: 
                    return True
                else:
                    l, r = l+1, r-1
            
            mid = (l+r) // 2
            if (nums[mid] >= nums[l]) == (target >= nums[l]):
                if target > nums[mid]:
                    l = mid+1
                elif target < nums[mid]:
                    r = mid
                else:
                    return True
            elif target >= nums[l]:
                r = mid
            else:
                l = mid + 1
        
        return False if nums[l] != target else True
