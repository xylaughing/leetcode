class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1: return 1 
        longest = float('-inf')
        ends = [-1]
        for i in range(len(nums)-1):
            if nums[i+1] > nums[i]:
                if i+1 == len(nums)-1:
                    longest = max(longest, i-ends[-1]+1)
            else:
                longest = max(longest, i-ends[-1])
                ends.append(i)
        return longest
