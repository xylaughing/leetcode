class Solution(object):
    def smallestNumber(self, num):
        """
        :type num: int
        :rtype: int
        """
        if -10 < num < 10: return num
        
        nums = list(str(num))
        if nums[0] == '-':
            nums = sorted(nums, reverse = True)
            return int(nums[-1] + ''.join(nums[:-1]))
        else:
            nums= sorted(nums)
            for i in range(len(nums)):
                if nums[i] != '0':
                    return int(nums[i] + ''.join(nums[0:i]) + ''.join(nums[i+1:]))
