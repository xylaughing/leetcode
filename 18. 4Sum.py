class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def sum3(nums, target):
            nums = sorted(nums)
            output = []
            for i in range(len(nums)-2):
                l, r = i+1, len(nums)-1
                while l < r:
                    if nums[l] + nums[r] == target - nums[i]:
                        if [nums[i], nums[l], nums[r]] not in output:
                            output.append([nums[i], nums[l], nums[r]])
                        l, r = l+1, r-1
                    elif nums[l] + nums[r] > target - nums[i]:
                        r -= 1
                    else:
                        l += 1
            return output
        
        output = []
        nums= sorted(nums)
        for i in range(len(nums)-3):
            if nums[i] not in nums[0:i]:
                temp = sum3(nums[i+1:], target - nums[i])
                if temp:
                    for x in temp:
                        output.append([nums[i]]+x)
        return output
