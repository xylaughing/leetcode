class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        output = []
        for i in range(len(nums)-2):
            l, r = i+1, len(nums)-1
            while l < r:
                if nums[l] + nums[r] == - nums[i]:
                    if [nums[i], nums[l], nums[r]] not in output:
                        output.append([nums[i], nums[l], nums[r]])
                    l, r = l+1, r-1
                elif nums[l] + nums[r] > - nums[i]:
                    r -= 1
                else:
                    l += 1
        return output
