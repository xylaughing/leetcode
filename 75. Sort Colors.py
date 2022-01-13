class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        """
        ct = Counter(nums)
        s = 0
        for x in ct:
            for j in range(s, s+ct[x]):
                nums[j] = x
            s += ct[x]
        return
        """
        zero, one, two = 0, 0, len(nums)-1
        while one <= two:
            if nums[one] == 0:
                nums[zero], nums[one] = nums[one], nums[zero]
                zero += 1
                one += 1
            elif nums[one] == 1:
                one += 1
            else:
                nums[one], nums[two] = nums[two], nums[one]
                two -= 1
        return 
        
