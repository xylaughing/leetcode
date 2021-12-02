class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        output = float('inf')
        for i in range(len(nums)-2):
            l, r = i+1, len(nums)-1
            while l < r:
                temp = nums[i] + nums[l] + nums[r]
                if abs(temp - target) < abs(output - target):
                    output = temp
                if temp == target:                    
                    return target
                elif temp > target:
                    r -= 1
                else:
                    l += 1
        return output       
