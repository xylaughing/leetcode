class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        """
        ct = Counter(nums)
        res = []
        for i in range(len(nums)):
            if not ct.has_key(i + 1): res.append(i+1)
        return res
        """
        """
        for i in range(len(nums)):
            ind = abs(nums[i]) - 1
            nums[ind] = -abs(nums[ind])
        return [i+1 for i in range(len(nums)) if nums[i] > 0]
        """
        
        ct = Counter(nums)
        return [i+1 for i in range(len(nums)) if not ct.has_key(i+1)]
