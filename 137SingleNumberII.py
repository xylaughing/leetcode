class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        return (sum(set(nums)) * 3 - sum(nums)) // 2
        
        """
        nums.sort()
        i = 0
        while i < len(nums)-2:
            if nums[i] == nums[i+2]:
                i += 3
            else:
                return nums[i]
        return nums[-1]
        """
        
        """
        for x, y in Counter(nums).items():
            if y == 1:
                return x
        """
