class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l, r = 0, len(nums) - 1
        output = []
        while l <= r:
            print("l, r", l, r)
            if nums[l]**2 > nums[r]**2:
                output.insert(0, nums[l]**2)
                l += 1
            else:
                output.insert(0, nums[r]**2)
                r -= 1      
                
        return output
