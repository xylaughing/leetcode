class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        def compare(a, b):
            return a + b > b + a
        
        nums = [str(x) for x in nums]
        for i in range(len(nums), 0, -1):
            for j in range(i-1):
                if not compare(nums[j], nums[j+1]):
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        return str(int(''.join(nums)))
