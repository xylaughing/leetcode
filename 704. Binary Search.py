class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        """
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        if target > nums[-1] or target < nums[0]:
            return -1       
        mid = len(nums) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.search(nums[0:mid], target)
        else:
            temp = self.search(nums[mid+1:], target)
            return mid+1+temp if temp != -1 else -1
        """
        if target > nums[-1] or target < nums[0]:
            return -1
        low, high = 0, len(nums)-1
        while low < high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        if low == high and nums[low] == target: return low
        return -1  
