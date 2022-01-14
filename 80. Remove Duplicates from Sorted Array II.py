class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 2
        for i in range(2, len(nums), 1):
            if nums[i] != nums[k-2]:
                nums[k] = nums[i]
                k += 1
        return k
