    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = len(nums)
        i = j = 1       # two pointer i and j
        for j in range(1, len(nums), 1):
            if nums[j] == nums[j-1]:    
                k = k - 1
            else:
                nums[i] = nums[j]
                i = i + 1
        return k
