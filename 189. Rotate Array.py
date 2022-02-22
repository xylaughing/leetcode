class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        """
        # O(k) extra space
        k = k % len(nums)
        temp = nums[len(nums)-k:]
        nums[k:] = nums[0:len(nums)-k]
        nums[0:k] = temp
        return
        """
        
        """
        k = k % len(nums)
        for i in range(k):
            tmp = nums[len(nums)-1]
            for j in range(len(nums)-2, -1, -1):
                nums[j+1] = nums[j]
            nums[0] = tmp]}
        return
        """
        
        def reverse(arr, l, r):
            while l < r:
                arr[l], arr[r] = arr[r], arr[l]
                l, r = l+1, r-1
            return
        
        k = k % len(nums)
        reverse(nums, 0, len(nums)-k-1)
        reverse(nums, len(nums)-k, len(nums)-1)
        reverse(nums, 0, len(nums)-1)
        return
