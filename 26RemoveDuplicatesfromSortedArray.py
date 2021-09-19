    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 1       # two pointer k and j
        for i in range(1, len(nums), 1):
            if nums[i] != nums[k-1]:
                nums[k] = nums[i]
                k += 1
        return k
