class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        maxs, temp = 0, 0
        for i in range(len(nums)):
            if nums[i] == 1: temp += 1
            else: 
                if maxs < temp: maxs = temp
                temp = 0
        return max(maxs, temp)
        """
        
        div = ''.join(map(str, nums)).split('0')
        return max(map(len, div))
